from b_tree.node import Node
from b_tree.sorted_table_map import SortedTableMap
import math


class MultiWaySearchTree:
    __slots__ = 'tree', 'node', 'root'

    def __init__(self, k, v):
        self.tree = SortedTableMap()
        self.node = Node(k, v, None, 10)
        self.tree.__setitem__(k, self.node)
        self.root = None
        self._root_node()

    def is_root(self, node):
        return node is self.root

    def _root_node(self):
        if self.tree.__len__() <= 1:
            self.root = self.tree._table[0]._key, self.tree._table[0]._value
        else:
            mid = self.tree.__len__() / 2
            if mid % 2 == 0:
                mid = math.floor(mid)
                self.root = self.tree._table[mid - 1]._key, self.tree._table[mid - 1]._value
            else:
                mid = math.floor(mid)
                self.root = self.tree._table[mid]._key, self.tree._table[mid]._value

    def is_empty(self):
        return self.node.stm.__len__() == 0

    # Max if brother is left and direction is True, Min if brother is right and direction is False
    def _transfer(self, brother, direction, father, istance):
        if direction:
            father.print_node()
            maximum_f = father.stm.find_max()
            if maximum_f is not None:
                print("Father-Son")
                print("Migration value: ", maximum_f[0])
                istance.insert_element(maximum_f[0], maximum_f[1])
                father.delete_element(maximum_f[0])
                self.fix_node()
                print()
                print("Son after insert")
                istance.print_node()
                print("Father after delete")
                father.print_node()
                print()
            maximum_b = brother.stm.find_max()
            if maximum_b is not None:
                print("Brother-Father")
                print("Migration value: ", maximum_b[0])
                father.insert_element(maximum_b[0], maximum_b[1])
                brother.delete_element(maximum_b[0])
                self.fix_node()
                print()
                print("Father after insert")
                father.print_node()
                print("Brother after delete")
                brother.print_node()
                print()
        else:
            father.print_node()
            minimum_f = father.stm.find_max()
            if minimum_f is not None:
                print("Father-Son")
                print("Migration value: ", minimum_f[0])
                istance.insert_element(minimum_f[0], minimum_f[1])
                father.delete_element(minimum_f[0])
                self.fix_node()
                print()
                print("Son after delete")
                istance.print_node()
                print("Father after delete")
                father.print_node()
                print()
            minimum_b = brother.stm.find_max()
            if minimum_b is not None:
                print("Brother-Father")
                print("Migration value: ", minimum_b[0])
                father.insert_element(minimum_b[0], minimum_b[1])
                brother.delete_element(minimum_b[0])
                self.fix_node()
                print()
                print("Father before insert")
                father.print_node()
                print("Brother after delete")
                brother.print_node()
                print()

    # side = false è sinistra, side = true è destro
    def _fusion(self, brother, direction, father, istance):
        istance_middle = istance.get_middle_element()
        self.tree.__delitem__(istance_middle[0])
        if direction:
            father.print_node()
            maximum_f = father.stm.find_max()
            if maximum_f is not None:
                print("Father-Son")
                print("Migration value: ", maximum_f[0])
                brother.insert_element(maximum_f[0], maximum_f[1])
                father.delete_element(maximum_f[0])
                self.fix_node()
                print()
                print("Figlio post inserimento")
                brother.print_node()
                print("Padre post cancellazione")
                father.print_node()
                print()
        else:
            father.print_node()
            minimum_f = father.stm.find_max()
            if minimum_f is not None:
                print("Father-Son")
                print("Migration value: ", minimum_f[0])
                brother.insert_element(minimum_f[0], minimum_f[1])
                father.delete_element(minimum_f[0])
                self.fix_node()
                print()
                print("Son before insert")
                brother.print_node()
                print("Father after delete")
                father.print_node()
                print()

    # If direction is True search on mid right tree, if direction is False search on mid left tree
    def find_first_util_node(self, k, direction):
        if direction:
            j = 0
            while j in range(len(self.tree), math.floor(len(self.tree) / 2)):
                if self.tree._table[j]._key > k and self.tree._table[j]._value.stm.__len__() > 0:
                    element = self.tree._table[j]._key, self.tree._table[j]._value
                    node = list(element)
                    return node[1]
                else:
                    j -= 1
            return self.root[1]
        else:
            i = math.floor(len(self.tree) / 2)
            while i in range(0, math.floor(len(self.tree) / 2)):
                if self.tree._table[i]._key > k and self.tree._table[i]._value.stm.__len__() > 0:
                    element = self.tree._table[i]._key, self.tree._table[i]._value
                    node = list(element)
                    return node[1]
                else:
                    i += 1
            return self.root[1]

    # If direction is True search on mid right tree, if direction is False search on mid left tree
    def search_other_node(self, k, direction):
        j = 0
        if direction:
            while j in range(math.floor(len(self.tree) / 2), len(self.tree)):
                if self.tree._table[j]._key > k and self.find_node(k, False) is not self.tree._table[j]._value:
                    element = self.tree._table[j]._key, self.tree._table[j]._value
                    node = list(element)
                    return node[1]
                else:
                    j += 1
        else:
            while j in range(0, math.floor(len(self.tree) / 2)):
                if self.tree._table[j]._key > k and self.find_node(k, False) is not self.tree._table[j]._value:
                    element = self.tree._table[j]._key, self.tree._table[j]._value
                    node = list(element)
                    return node[1]
                else:
                    j += 1

    # If direction is True search right brother, if direction is False search left brother
    def search_siblings(self, k, direction):
        if direction is True:
            element = self.tree.find_gt(k)
            if element is None:
                return None
            else:
                node = list(element)
                return node[1]
        else:
            element = self.tree.find_gt(self.root[0])
            if element is None:
                return None
            else:
                node = list(element)
                return node[1]

    def verify_underflow(self, k, node):
        if node.underflow == 1:
            print("Underflow")
            if k > self.root[0]:
                element = self.find_first_util_node(k, True)
            else:
                element = self.find_first_util_node(k, False)
            print("Element: ", element)
            if element is not None:
                right_brother = self.search_siblings(k, True)
                left_brother = self.search_siblings(k, False)
                print("Right brother: ", right_brother)
                print("Left brother: ", left_brother)
                if right_brother is not None:
                    print()
                    print("Right brother not None")
                    if right_brother.stm.__len__() == 1:
                        if right_brother is element:
                            print("Father is brother")
                        print()
                        print("Invoke right fusion")
                        self._fusion(k, right_brother, False, element, node)
                    else:
                        if right_brother is element:
                            print("Father is brother")
                        print()
                        print("Invoke right transfer")
                        self._transfer(right_brother, False, element, node)
                elif left_brother is not None:
                    print()
                    print("Left brother not None")
                    if left_brother.stm.__len__() == 1:
                        if left_brother is element:
                            print("Father is brother")
                        print()
                        print("Invoke left fusion")
                        self._fusion(k, left_brother, True, element, node)
                    else:
                        if left_brother is element:
                            print("Father is brother")
                        print()
                        print("Invoke left transfer")
                        self._transfer(left_brother, True, element, node)
                else:
                    print("Mistake")
            else:
                print("Without father")

    def delete_tree_element(self, k):
        print()
        print("Delete element: ", k)
        node = self.find_node(k, False)
        self.node = node
        if k >= self.root[0]:
            maximum = self.tree.find_max()
            other_node = self.search_other_node(k, True)
            if maximum[1] is self.node:
                print("Delete node")
                self.node.print_node()
                print()
                self.node.delete_element(k)
                self.fix_node()
                self.verify_underflow(k, self.node)
                print("After delete")
                self.node.print_node()
            elif other_node is not None:
                print("Is not leaf")
                print("Delete node")
                self.node.print_node()
                print("Exchange node")
                other_node.print_node()
                print()
                self.node.delete_element(k)
                minimum = other_node.stm.find_min()
                self.node.stm.__setitem__(minimum[0], minimum[1])
                other_node.delete_element(minimum[0])
                self.fix_node()
                self.verify_underflow(k, self.node)
                self.verify_underflow(k, other_node)
                print("After delete")
                self.node.print_node()
                other_node.print_node()
            else:
                print("Is not leaf")
                print("Delete node")
                self.node.print_node()
                print("Exchange node")
                other_node = self.tree.find_max()[1]
                other_node.print_node()
                print()
                other_middle = other_node.get_middle_element()
                inorder_element = other_node.stm.find_min()
                self.node.delete_element(k)
                self.node.insert_element(inorder_element[0], inorder_element[1])
                other_node.delete_element(inorder_element[0])
                self.fix_node()
                self.verify_underflow(k, self.node)
                self.verify_underflow(k, other_node)
        else:
            minimum = self.tree.find_min()
            other_node = self.search_other_node(k, False)
            if minimum[1] is self.node:
                print("Delete node")
                self.node.print_node()
                print()
                self.node.delete_element(k)
                self.fix_node()
                self.verify_underflow(k, self.node)
                print("After delete")
                self.node.print_node()
            elif other_node is not None:
                print("Is not leaf")
                print("Delete node")
                self.node.print_node()
                print("Exchange node")
                other_node.print_node()
                other_middle = other_node.get_middle_element()
                self.node.delete_element(k)
                minimum_node = other_node.find_min()
                self.node.stm.__setitem__(minimum_node[0], minimum_node[1])
                other_node.delete_element(minimum_node[0])
                self.fix_node()
                self.verify_underflow(k, self.node)
                self.verify_underflow(k, other_node)
                print("After delete")
                self.node.print_node()
                other_node.print_node()

    def _split(self, node):
        print("Split invoked")
        copy_node = node
        middle_element = copy_node.get_middle_element()
        first = copy_node.stm.find_gt(middle_element[0])
        new_node = Node(first[0], first[1], copy_node._parent, 10)
        print("NEW NODE")
        new_node.print_node()
        copy_node.stm.__delitem__(first[0])
        print("OLD NODE")
        copy_node.print_node()
        while copy_node.stm.find_gt(middle_element[0]) is not None:
            element = copy_node.stm.find_gt(middle_element[0])
            new_node.insert_element(element[0], element[1])
            print("NEW NODE")
            new_node.print_node()
            copy_node.stm.__delitem__(element[0])
            print("OLD NODE")
            copy_node.print_node()
        copy_node.delete_element(middle_element[0])
        copy = copy_node.stm.find_min()
        split_node = Node(copy[0], copy[1], None, 10)
        while copy_node.stm.__len__() > 0:
            element = copy_node.stm.find_min()
            split_node.insert_element(element[0], element[1])
            copy_node.delete_element(element[0])
        if self.tree.__len__() <= 1:
            print("Is root")
            new_root = Node(middle_element[0], middle_element[1], None, 10)
            new_node._parent = new_root
            split_node._parent = new_root
            print("Middle element of the splitted node ", copy_node.get_middle_element()[0])
            self.tree.__setitem__(split_node.get_middle_element()[0], split_node)
            self.tree.__setitem__(new_node.get_middle_element()[0], new_node)
            self.tree.__setitem__(new_root.get_middle_element()[0], new_root)
            self.fix_node()
            self._root_node()
            print("Old Node/Root")
            split_node.print_node()
            print("Padre", split_node._parent)
            print("New root")
            new_root.print_node()
            print("Father", new_root._parent)
            print("New node")
            new_node.print_node()
            print("Father", new_node._parent)
            print()
        else:
            print("Is not root")
            new_node._parent = copy_node._parent
            split_node._parent = copy_node._parent
            self.node = copy_node._parent
            self.node.insert_element(middle_element[0], middle_element[1])
            self.tree.__setitem__(split_node.get_middle_element()[0], split_node)
            self.tree.__setitem__(new_node.get_middle_element()[0], new_node)
            self.fix_node()

    def fix_node(self):
        j = 0
        while j in range(0, len(self.tree) - 1):
            copy = self.tree._table[j]._key, self.tree._table[j]._value
            node = list(copy)
            if node[1].get_middle_element()[0] is None:
                self.tree.__delitem__(node[0])
            else:
                new_middle = node[1].get_middle_element()
                self.tree.__delitem__(self.tree._table[j]._key)
                self.tree.__setitem__(new_middle[0], node[1])
            j += 1

    def new_element(self, k, v):
        print("Insert element: ", k, " ", v)
        node = self.find_node(k, True)
        self.node = node
        self.node.insert_element(k, v)
        self.fix_node()
        if self.node.overflow == 1:
            self._split(self.node)

    # type is True on insert and False on delete
    def find_node(self, k, type):
        t = self.tree.find_ge(k)
        if t is None:
            if type is True:
                t = self.tree.find_lt(k)
            else:
                t = self.tree.find_max()
        node = list(t)
        return node[1]

    def print_tree(self):
        print("Print tree")
        for j in range(0, len(self.tree)):
            print("(", self.tree._table[j]._key, ",", self.tree._table[j]._value, ")")
            print()
            self.tree._table[j]._value.print_node()
            print()

    def num_nodes(self):
        return self.tree.__len__()
