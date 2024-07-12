
##SALIDAS DEL EJERCICIO 2 :

(tutorial-env) anderson@anderson-IdeaPad-Flex-5-14ABR8:~/Escritorio/ExamFinal-C8286$ python3 ejercicio2.py 
Ejecutando Raft:
Raft log: []

Ejecutando Chandy-Lamport:
Node 0 received Marker from 1
Node 2 received Marker from 1
Node 3 received Marker from 1
Node 4 received Marker from 1

Ejecutando Raymond Mutex:
Traceback (most recent call last):
  File "/home/anderson/Escritorio/ExamFinal-C8286/ejercicio2.py", line 153, in <module>
    raymond_nodes[0].send_request()
  File "/home/anderson/Escritorio/ExamFinal-C8286/ejercicio2.py", line 77, in send_request
    for node in nodes:
                ^^^^^
NameError: name 'nodes' is not defined. Did you mean: 'node'?


##SALIDAS DEL EJERCICIO 3 :

(tutorial-env) anderson@anderson-IdeaPad-Flex-5-14ABR8:~/Escritorio/ExamFinal-C8286$ python3 ejercicio3.py 
Ejecutando Raft:
Raft log: []

Ejecutando Chandy-Lamport:
Node 0 received Marker from 1
Node 2 received Marker from 1
Node 3 received Marker from 1
Node 4 received Marker from 1

Ejecutando Cristian:
Node 0 synchronized clock: 2024-07-12 17:56:03.347894
Node 1 synchronized clock: 2024-07-12 17:56:03.347894
Node 2 synchronized clock: 2024-07-12 17:56:03.347894
Node 3 synchronized clock: 2024-07-12 17:56:03.347894
Node 4 synchronized clock: 2024-07-12 17:56:03.347894

Asignado obj1 en: 0
Recoleccion de basura completa


##SALIDAS DEL EJERCICIO 4 :

(tutorial-env) anderson@anderson-IdeaPad-Flex-5-14ABR8:~/Escritorio/ExamFinal-C8286$ python3 ejercicio4.py 
Node 0 read key0: value0
Node 1 read key1: value1
Node 2 read key2: value2
Node 3 read key3: value3
Node 0 read key4: value4
Ejecutando Paxos:
Agreed Value: Update Inventory Record

Simulating CP mode
Node 0 read key0: value0
Node 1 read key1: value1
Node 0 read key4: value4

