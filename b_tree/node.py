from b_tree.sorted_table_map import SortedTableMap
import math


class Node:
    __slots__ = 'stm', '_middle', '_parent', '_d', 'overflow', 'underflow'

    def __init__(self, k, v, p, d):
        super().__init__()
        self.stm = SortedTableMap()
        self.stm.__setitem__(k, v)
        self._parent = p
        self._middle = None
        self._middle_element()
        self._d = d
        self.overflow = 0
        self.underflow = 0

    def _middle_element(self):
        if self.stm.__len__() == 1:
            self._middle = self.stm._table[0]._key, self.stm._table[0]._value
        elif self.stm.__len__() == 0:
            self._middle = None, None
        else:
            mid = self.stm.__len__() / 2
            if mid % 2 == 0:
                mid = math.floor(mid)
                self._middle = self.stm._table[mid - 1]._key, self.stm._table[mid - 1]._value
            else:
                mid = math.floor(mid)
                self._middle = self.stm._table[mid]._key, self.stm._table[mid]._value

    def get_middle_element(self):
        if self._middle is None:
            return None
        else:
            return self._middle

    def insert_element(self, k, v):
        if self.stm.__len__() == 0:
            self.stm.__setitem__(k, v)
            self._middle_element()
            self.underflow = 0
        if 0 < self.stm.__len__() < self._d:
            self.stm.__setitem__(k, v)
            self._middle_element()
        else:
            self.stm.__setitem__(k, v)
            self._middle_element()
            self.overflow = 1

    def delete_element(self, k):
        if self.stm.__len__() >= 1:
            self.stm.__delitem__(k)
            self._middle_element()
        else:
            print("Mistake")
        if len(self.stm._table) == 0:
            self.underflow = 1

    def print_node(self):
        for j in range(0, len(self.stm)):
            print("(", self.stm._table[j]._key, ",", self.stm._table[j]._value, ")")
        print("Middle element: ", self.get_middle_element()[0])

