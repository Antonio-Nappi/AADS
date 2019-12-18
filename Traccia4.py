import copy
from tree.concrete_tree import ConcreteTree


def color_node(tree):
    a = []
    i = 0
    for p in tree.preorder():
        p.set_array_pos(i)
        a.append((p, copy.deepcopy(tree.num_children(p))))
        i += 1
    for i in range(len(a) - 1, -1, -1):
        if a[i][1] > 0:
            a[i][0].color()
            #vedere solo se il parent all'interno del nodo restituisce la position oppure un nodo, se è un nodo va bene, altrimenti bisogna scrivere
            #self._node._parent._node._numb (in concrete tree metodo get_parent_position)
            pos = a[i][0].get_parent_pos()
            a[pos][1] -= 1
