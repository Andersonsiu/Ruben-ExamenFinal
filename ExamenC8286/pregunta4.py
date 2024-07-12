import random
import threading
import time

#consistencia
class PaxosNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.proposal_number = 0
        self.accepted_proposal_number = -1
        self.accepted_value = None
        self.promised_proposal_number = -1

    def prepare(self, proposal_number):
        if proposal_number > self.promised_proposal_number:
            self.promised_proposal_number = proposal_number
            return self.accepted_proposal_number, self.accepted_value
        return None

    def accept(self, proposal_number, value):
        if proposal_number >= self.promised_proposal_number:
            self.promised_proposal_number = proposal_number
            self.accepted_proposal_number = proposal_number
            self.accepted_value = value
            return True
        return False

    def consensus(self, nodes, value):
        self.proposal_number += 1
        promises = []
        for node in nodes:
            promise = node.prepare(self.proposal_number)
            if promise:
                promises.append(promise)
        
        if len(promises) > len(nodes) // 2:
            for node in nodes:
                node.accept(self.proposal_number, value)
            self.accepted_value = value
        return self.accepted_value

def simulate_paxos(nodes, value):
    leader = random.choice(nodes)
    consensus_value = leader.consensus(nodes, value)
    return consensus_value


#simulacion and partition
class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.data = {}
        self.lock = threading.Lock()

    def write(self, key, value):
        with self.lock:
            self.data[key] = value

    def read(self, key):
        with self.lock:
            return self.data.get(key, None)

class NetworkPartition:
    def __init__(self, nodes):
        self.nodes = nodes

    def create_partition(self):
        partitioned_nodes = random.sample(self.nodes, len(self.nodes) // 2)
        for node in partitioned_nodes:
            node.lock.acquire()

    def resolve_partition(self):
        for node in self.nodes:
            if node.lock.locked():
                node.lock.release()

def simulate_cap(nodes, mode):
    partition = NetworkPartition(nodes)
    if mode in ["CP", "AP"]:
        partition.create_partition()
    
    def writer(node, key, value):
        node.write(key, value)
        time.sleep(random.random())

    def reader(node, key):
        value = node.read(key)
        print(f"Node {node.node_id} read {key}: {value}")

    threads = []
    for i in range(5):
        writer_thread = threading.Thread(target=writer, args=(nodes[i % len(nodes)], f"key{i}", f"value{i}"))
        reader_thread = threading.Thread(target=reader, args=(nodes[i % len(nodes)], f"key{i}"))
        threads.append(writer_thread)
        threads.append(reader_thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    if mode in ["CP", "AP"]:
        partition.resolve_partition()

#consistencia eventual
class EventualConsistencyNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.data = {}
        self.lock = threading.Lock()

    def write(self, key, value):
        with self.lock:
            self.data[key] = value

    def read(self, key):
        with self.lock:
            return self.data.get(key, None)

    def synchronize(self, other_node):
        with self.lock, other_node.lock:
            for key, value in other_node.data.items():
                if key not in self.data:
                    self.data[key] = value

def simulate_eventual_consistency(nodes):
    def writer(node, key, value):
        node.write(key, value)
        time.sleep(random.random())

    def reader(node, key):
        value = node.read(key)
        print(f"Node {node.node_id} read {key}: {value}")

    def synchronizer(node1, node2):
        node1.synchronize(node2)
        time.sleep(random.random())

    threads = []
    for i in range(5):
        writer_thread = threading.Thread(target=writer, args=(nodes[i % len(nodes)], f"key{i}", f"value{i}"))
        reader_thread = threading.Thread(target=reader, args=(nodes[i % len(nodes)], f"key{i}"))
        sync_thread = threading.Thread(target=synchronizer, args=(nodes[i % len(nodes)], nodes[(i + 1) % len(nodes)]))
        threads.append(writer_thread)
        threads.append(reader_thread)
        threads.append(sync_thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    nodes = [EventualConsistencyNode(i) for i in range(4)]
    simulate_eventual_consistency(nodes)

if __name__ == "__main__":

    #Ejecutar Paxos
    print("Ejecutando Paxos:")
    paxos_nodes = [PaxosNode(i) for i in range(5)]
    paxos_value = "Update Inventory Record"
    agreed_value = simulate_paxos(paxos_nodes, paxos_value)
    print(f"Agreed Value: {agreed_value}\n")
    
    #Simulacion
    nodes = [Node(i) for i in range(4)]
    print("Simulating CP mode")
    simulate_cap(nodes, "CP")
    print("\nSimulating AP mode")
    simulate_cap(nodes, "AP")
    print("\nSimulating CA mode")
    simulate_cap(nodes, "CA")
    
    #tolerancia fallos
    print("Ejecutando Tolerancia a Fallos Bizantina:")
    byzantine_nodes = [ByzantineNode(i, is_faulty=(i % 2 == 0)) for i in range(5)]
    simulate_byzantine(byzantine_nodes)
    print()
    
