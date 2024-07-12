import threading
import random
import queue
import time
from datetime import datetime, timedelta

# Algoritmo de Raft 

class RaftNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.term = 0
        self.voted_for = None
        self.log = []

    def request_vote(self, term, candidate_id):
        if term > self.term:
            self.term = term
            self.voted_for = candidate_id
            return True
        return False

    def append_entries(self, term, leader_id, entries):
        if term >= self.term:
            self.term = term
            self.log.extend(entries)
            return True
        return False

def simulate_raft(nodes, entries):
    leader = random.choice(nodes)
    for node in nodes:
        if node != leader:
            node.append_entries(leader.term, leader.node_id, entries)
    return leader.log

# Algoritmo de Chandy-Lamport

class ChandyLamportNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.state = None
        self.channel = queue.Queue()

    def record_state(self):
        self.state = f"State of node {self.node_id}"

    def send_marker(self, nodes):
        for node in nodes:
            if node != self:
                node.channel.put(f"Marker from {self.node_id}")

    def receive_marker(self):
        while not self.channel.empty():
            marker = self.channel.get()
            print(f"Node {self.node_id} received {marker}")

def simulate_chandy_lamport(nodes):
    initiator = random.choice(nodes)
    initiator.record_state()
    initiator.send_marker(nodes)
    for node in nodes:
        node.receive_marker()

# Exclusion Mutua
class RaymondMutexNode:
    def __init__(self, node_id, num_nodes):
        self.node_id = node_id
        self.num_nodes = num_nodes
        self.clock = 0
        self.request_queue = queue.PriorityQueue()
        self.replies_received = 0

    def send_request(self):
        self.clock += 1
        self.request_queue.put((self.clock, self.node_id))
        for node in nodes:
            if node.node_id != self.node_id:
                node.receive_request(self.clock, self.node_id)

    def receive_request(self, timestamp, sender_id):
        self.clock = max(self.clock, timestamp) + 1
        self.request_queue.put((timestamp, sender_id))
        self.send_reply(sender_id)

    def send_reply(self, target_id):
        for node in nodes:
            if node.node_id == target_id:
                node.receive_reply(self.node_id)

    def receive_reply(self, sender_id):
        self.replies_received += 1
        if self.replies_received == self.num_nodes - 1:
            self.enter_critical_section()

    def enter_critical_section(self):
        print(f"Node {self.node_id} entering critical section")
        time.sleep(1)
        self.leave_critical_section()

    def leave_critical_section(self):
        print(f"Node {self.node_id} leaving critical section")
        self.replies_received = 0
        self.request_queue.get()

#Recolector Basura
class CheneyCollector:
    def __init__(self, size):
        self.size = size
        self.from_space = [None] * size
        self.to_space = [None] * size
        self.free_ptr = 0

    def allocate(self, obj):
        if self.free_ptr >= self.size:
            self.collect()
        addr = self.free_ptr
        self.from_space[addr] = obj
        self.free_ptr += 1
        return addr

    def collect(self):
        self.to_space = [None] * self.size
        self.free_ptr = 0
        for obj in self.from_space:
            if obj is not None:
                self.copy(obj)
        self.from_space, self.to_space = self.to_space, self.from_space

    def copy(self, obj):
        addr = self.free_ptr
        self.to_space[addr] = obj
        self.free_ptr += 1
        return addr

if __name__ == "__main__":
    # Ejecutar Raft
    print("Ejecutando Raft:")
    raft_nodes = [RaftNode(i) for i in range(5)]
    raft_entries = ["Transaction 1", "Transaction 2"]
    raft_log = simulate_raft(raft_nodes, raft_entries)
    print(f"Raft log: {raft_log}\n")

    # Ejecutar Chandy-Lamport
    print("Ejecutando Chandy-Lamport:")
    chandy_nodes = [ChandyLamportNode(i) for i in range(5)]
    simulate_chandy_lamport(chandy_nodes)
    print()
    
    # Ejecutar Raymond
    print("Ejecutando Raymond Mutex:")
    raymond_nodes = [RaymondMutexNode(i, 3) for i in range(3)]
    raymond_nodes[0].send_request()
    print()
    
    # Recolector de Basura
    collector = CheneyCollector(10)
    addr1 = collector.allocate("obj1")
    print(f"Asignado obj1 en: {addr1}")
    collector.collect()
    print("Recoleccion de basura completa")
