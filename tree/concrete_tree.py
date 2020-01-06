from tree.tree import Tree

class ConcreteTree(Tree):

    """Linked representation of a tree structure."""
    
  #-------------------------- nested _Node class --------------------------
    
    class _Node:
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_element', '_parent', '_children', '_colored', '_pos'

        def __init__(self, element, parent=None, children=None):
            self._element = element
            self._parent = parent
            self._children = children
            if self._children is None:
                self._children = []
            self._colored = False
            self._pos = 0

  #-------------------------- nested Position class --------------------------
    
    class Position(Tree.Position):
        """An abstraction representing the location of a single element."""
        def __init__(self, container, node):
          """Constructor should not be invoked by user."""
          self._container = container
          self._node = node
          
        def element(self):
          """Return the element stored at this Position."""
          return self._node._element

        def get_parent_position(self):
            return self.node()._parent._pos

        def node(self):
            return self._node

        def color(self):
            self._node._colored = True

        def set_array_position(self, index):
            self._node._pos = index

        def __str__(self):
            return "Element {} colored: {}".format(self.element(),self.node()._colored)

        def __eq__(self, other):
          """Return True if other is a Position representing the same location."""
          return type(other) is type(self) and other._node is self._node
# ------------------------------- utility methods -------------------------------
    
    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
          raise TypeError('p must be proper Position type')
        if p._container is not self:
          raise ValueError('p does not belong to this container')
        if p._node._parent is p._node: #convention for deprecated nodes
          raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None
    
    def __init__(self):
        """Create an initially empty tree."""
        self._root = None
        self._size = 0

  #-------------------------- public accessors --------------------------
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def children(self, p):
        l = []
        for e in p._node._children:
            l.append(self._make_position(e))
        return l

  #-------------------------- nonpublic mutators --------------------------
    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.
        Raise ValueError if tree nonempty.
        """
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add(self, p, e):
        """Create a new child for Position p, storing element e.
        Return the Position of new node.
        """
        self._size += 1
        node = self._Node(e, p._node)
        p._node._children.append(node)
        return self._make_position(node)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        for f in node._children:
            count += 1
        return count



