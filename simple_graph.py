# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function


class SimpleGraph(object):
    """Implementation of a simple, directed, un-weighted graph."""
    def __init__(self):
        """Create an empty graph."""
        self.graph = {}

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return [k for k in self.graph.keys()]

    def edges(self):
        """Return a list of all edges in the graph."""
        my_edges = []
        for k, v in self.graph.iteritems():
            for node in v:
                my_edges.append((k, node))
        return my_edges

    def add_node(self, n):
        """Add a new node 'n' to the graph."""
        self.graph[n] = []

    def add_edge(self, n1, n2):
        """Add a new edge to the graph connecting 'n1' and 'n2'.

        'n1' points to 'n2'

        If either n1 or n2 are not already present in the graph,
        they should be added.
        """

        # check if nodes exist
        if n1 not in self.graph:
            self.add_node(n1)
        if n2 not in self.graph:
            self.add_node(n2)

        # check if edge already exists
        if n2 not in self.graph[n1]:
            self.graph[n1].append(n2)

    def del_node(self, n):
        """Delete the node 'n' from the graph.

        Raises an error if no such node exists.
        """
        del self.graph[n]
        for k, v in self.graph.iteritems():
            if n in v:
                del v[v.index(n)]

    def del_edge(self, n1, n2):
        """Delete the edge connecting 'n1' and 'n2' from the graph.

        Raises an error if no such edge exists.
        """
        del self.graph[n1][self.graph[n1].index(n2)]

    def has_node(self, n):
        """Return True if node 'n' is contained in the graph."""
        return n in self.graph.keys()

    def neighbors(self, n):
        """Return the list of all nodes connected to 'n' by edges.

        'n' points to its neighbors

        Raises an error if 'n' is not in the graph.
        """
        if n in self.graph:
            return self.graph[n]
        else:
            raise KeyError('Neighbors: Node not in graph.')

    def adjacent(self, n1, n2):
        """Return True if there is an edge connecting 'n1' and 'n2'.

        'n1' points to 'n2'

        Raises an error if either of the supplied nodes are not in the graph.
        """
        if n1 not in self.graph or n2 not in self.graph:
            raise IndexError('Adjacent: At least one node not found.')
        return n2 in self.graph[n1]

    def depth_first_traversal(self, start):
        """Perform a full depth first traversal of the graph starting
        at 'start'.

        Return the full visited path when the traversal is complete
        as a list.
        """
        path = []
        queue = [start]

        while queue:
            node = queue.pop(0)
            if node not in path:
                path.append(node)
                queue = self.neighbors(node) + queue
        return path

    def breadth_first_traversal(self, start):
        """Perform a full breadth first traversal of the graph starting
        at 'start'.

        Return the full visited path when the traversal is complete
        as a list.
        """
        path = []
        queue = [start]

        while queue:
            node = queue.pop(0)
            if node not in path:
                path.append(node)
                queue = queue + self.neighbors(node)
        return path

if __name__ == '__main__':
    g = SimpleGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('c', 'f')
    g.add_edge('g', 'f')
    g.add_edge('a', 'd')
    g.add_edge('d', 'e')
    g.add_edge('e', 'a')
    print("df1: " + repr(g.depth_first_traversal('a')))
    print("bf1: " + repr(g.breadth_first_traversal('a')))

    g2 = SimpleGraph()
    g2.add_edge('a', 'b')
    g2.add_edge('a', 'c')
    g2.add_edge('a', 'e')
    g2.add_edge('b', 'd')
    g2.add_edge('b', 'f')
    g2.add_edge('f', 'e')
    g2.add_edge('c', 'g')
    print("df2: " + repr(g2.depth_first_traversal('a')))
    print("bf2: " + repr(g2.breadth_first_traversal('a')))
