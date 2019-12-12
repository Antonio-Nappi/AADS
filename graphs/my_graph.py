from graphs.graph import Graph


class My_graph(Graph):

    class Vertex(Graph.Vertex):
        """Lightweight vertex structure for a graph."""
        __slots__ = '_colored'

        def __init__(self, x, colored=False):
            """Do not call constructor directly. Use Graph's insert_vertex(x)."""
            super().__init__(x)
            self._colored = colored

        def colored(self):
            """Return color associated with this vertex."""
            return self._colored

        def color(self):
            """Color the specific vertex"""
            self._colored = True

        def __str__(self):
            return "Nodo {0} colore {1}".format(self._element,self._colored)

    def not_colored_vertex(self, v):
        for edge in self.incident_edges(v):
            other = edge.opposite(v)
            if not other.colored():
                yield other

    def get_vertices(self):
        return list(self.vertices())

    def not_colored_degree(self, v, outgoing=True):
        self._validate_vertex(v)
        c = 0
        adj = self._outgoing if outgoing else self._incoming
        for vertex in adj[v]:
            if vertex.colored():
                c += 1
        #print("gli archi colorati del vertice {} sono: {}".format(v.element(), c))
        return len(adj[v]) - c
