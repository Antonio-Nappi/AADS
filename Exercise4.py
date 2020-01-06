from tree.concrete_tree import ConcreteTree

def color_node(tree):
    a = []
    i = 0
    for p in tree.preorder():
        p.set_array_position(i)
        a.append([p, tree.num_children(p)])
        i += 1
    for i in range(len(a) - 1, -1, -1):
        if a[i][1] > 0:
            #vedere solo se il parent all'interno del nodo restituisce la position oppure un nodo, se è un nodo va bene, altrimenti bisogna scrivere
            #self._node._parent._node._numb (in concrete tree metodo get_parent_position)
            a[i][0].color()
            pos = a[i][0].get_parent_position()
            a[pos][1] -= 1


#little example
t2 = ConcreteTree()
t2._add_root(1)
x4 = t2._add(t2.root(), 4)
x6 = t2._add(t2.root(), 6)
x7 = t2._add(t2.root(), 7)
x10 = t2._add(x4, 10)
x8 = t2._add(x4, 8)
x24 = t2._add(x6, 24)
x3 = t2._add(x7, 3)
x9 = t2._add(x10, 9)
color_node(t2)
print("Execution of the algorithm")
for p in t2.preorder():
    print(p)