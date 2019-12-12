import random
import time
from graphs.my_graph import My_graph
def color_vertex(graph):
    for vertex in graph.vertices():
        print("nodo esterno: ", vertex.element())
        if vertex.colored():
            continue
        for v in graph.not_colored_vertex(vertex):
            if graph.degree(vertex) >= graph.degree(v):#non graph.degree(vertex) ma dobbiamo sottrarre il degree se l'edge dall'altra parte è già colorato
                vertex.color()
                break
            else:
                v.color()


graph = My_graph()
for i in range(10):
    graph.insert_vertex(i)

for vertex in graph.vertices():
    for v in graph.vertices():
        if not(v == vertex or (graph.get_edge(vertex, v) is not None)):
            if random.randint(0, 5) == 0:
                graph.insert_edge(vertex, v)
                print(graph.get_edge(vertex, v))

for ver in graph.vertices():
    print("outDegree del vertice {}: {}".format(ver.element(), graph.degree(ver)))


t = time.time() * 1000
color_vertex(graph)
t2 = time.time() * 1000
colored = 0
for v in graph.vertices():
    if v.colored():
        colored = colored + 1
    print(v)

print(t2-t, "ms")
print("I nodi colorati sono {}".format(colored))



