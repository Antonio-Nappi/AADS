import numpy as np
from tree.concrete_tree import ConcreteTree

def color_node(tree):
    a = []
    for n in tree.preorder():
        a.append(n._Node._children)
        #riferimento al nodo
        #riferimento al padre
    for i in range(len(a), 0):
        if a[i] > 0:
            colora il nodo
            decrementa di uno il padre
