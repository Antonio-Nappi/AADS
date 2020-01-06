from .map_base import MapBase

class SortedTableMap(MapBase):

    def _find_index(self, k, low, high):
        if high < low:
            return high + 1
        else:
            mid = (low + high) // 2
            if k == self._table[mid]._key:
                return mid
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid - 1)
            else:
                return self._find_index(k, mid + 1, high)

    def __init__(self):
        self._table = []

    def __len__(self):
        return len(self._table)

    def __getitem__(self, key):
        j = self._find_index(key, 0, len(self._table) -1)
        if j == len(self._table) or self._table[j]._key != key:
            raise KeyError('Key Error: ' + repr(key))
        return self._table[j]._value

    def __setitem__(self, key, value):
        j = self._find_index(key, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == key:
            self._table[j]._value = value
        else:
            self._table.insert(j, self._Item(key, value))

    def __delitem__(self, key):
        j = self._find_index(key, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != key:
            raise KeyError('Key Error: ' + repr(key))
        self._table.pop(j)

    def __iter__(self):
        for item in self._table:
            yield item._key

    def __reversed__(self):
        for item in reversed(self._table):
            yield item._key

    def find_key(self, k, low, high):
        if high < low:
            return None
        else:
            mid = (low + high) // 2
            if k == self._table[mid]._key:
                return mid
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid - 1)
            else:
                return self._find_index(k, mid + 1, high)

    def find_min(self):
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        if len(self._table) > 0:
            return self._table[-1]._key, self._table[-1]._value
        else:
            return None

    def find_le(self, key):
        j = self._find_index(key, 0, len(self._table) - 1)
        if j > 0 and self._table[j]._key  == key:
            return (self._table[j]._key, self._table[j]._value)
        if j == 0 and self._table[j]._key < key:
            return (self._table[j].key, self._table[j]._value)
        else:
            return None

    def find_ge(self, key):
        j = self._find_index(key, 0, len(self._table) - 1)
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_lt(self, key):
        j = self._find_index(key, 0, len(self._table) - 1)
        if j > 0:
            return (self._table[j-1]._key, self._table[j-1]._value)
        else:
            return None

    def find_gt(self, key):
        j = self._find_index(key, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == key:
            j += 1
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_range(self, start, stop):
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self._table) - 1)
        while j < len(self._table) and (stop is None or self._table[j]._key < stop):
            yield (self._table[j]._key, self._table[j]._value)
            j += 1
