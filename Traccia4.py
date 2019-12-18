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
            #vedere solo se il parent all'interno del nodo restituisce la position oppure un nodo, se è un nodo va bene, altrimenti bisogna scrivere
            #self._node._parent._node._numb (in concrete tree metodo get_parent_position)
            pos = a[i][0].get_parent_pos()
            a[pos][1] -= 1
        else:
            a[i][0].colorF()



def v_color(tree):
    if tree.root() == None:
        return 0
    if tree.num_children(tree.root()) == 0:
        tree.root().colorF()
        return 0
    if tree.num_childrenC(tree.root()) == 0:
        tree.root().colorF()
        return 0

    if tree.root().node().vc() != 0:
        return tree.root().node().vc()

    a = 0
    for f in tree.root().node()._children:
        a += v_color(f)
    sizei = 1 + a

    sizeo = 0
    b = 0
    for f in tree.root().node()._children:
        b += 1 + v_color(f)

    tree.root().node().svc(min(sizei, sizeo))
    return tree.root().node().vc()
