import copy
from tree.concrete_tree import ConcreteTree


def color_node(tree):
    a = []
    i = 0
    for p in tree.preorder():
        p.set_array_pos(i)
        a.append((p, copy.deepcopy(tree.num_children(p))))
        i += 1
    for i in range(len(a), 0):
        if a[i][1] > 0:
            a[i][0].color()
            pos = a[i][0].array_pos()
            a[pos][1] -= 1
