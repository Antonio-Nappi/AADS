from graphs.graph import Graph


class My_graph(Graph):

    class Vertex(Graph.Vertex):
        """Lightweight vertex structure for a graph."""
        __slots__ = '_colored','_pre'

        def __init__(self, x, colored=False,pre=None):
            """Do not call constructor directly. Use Graph's insert_vertex(x)."""
            super().__init__(x)
            self._colored = colored
            self._pre=pre

        def colored(self):
            """Return color associated with this vertex."""
            return self._colored

        def color(self):
            """Color the specific vertex"""
            self._colored = True

        def pre(self):
            """Return the precedent element."""
            return self._pre

        def set_pre(self, x=None):
            self._pre = x

        def __str__(self):
            """Used to show to the user the element and if the Vertex is colored or not."""
            return "Vertex {} color {}".format(self._element,self._colored)

    def not_colored_vertex(self, v):
        """Iterator over the vertices, connected to the vertex v, those are not colored."""
        self._validate_vertex(v)
        for edge in self.incident_edges(v):
            other = edge.opposite(v)
            if not other.colored():
                yield other

    def not_colored_degree(self, v):
        """Return the number of vertex not colored connected to the vertex v."""
        self._validate_vertex(v)
        return len(list(self.not_colored_vertex(v)))


