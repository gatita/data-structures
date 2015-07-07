# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function


class SimpleGraph(object):
    """Implementation of a simple, directed, un-weighted graph."""
    def __init__(self):
        """Create an empty graph."""
        pass

    def nodes(self):
        """Return a list of all nodes in the graph."""
        pass

    def edges(self):
        """Return a list of all edges in the graph."""
        pass

    def add_node(self, n):
        """Add a new node 'n' to the graph."""
        pass

    def add_edge(self, n1, n2):
        """Add a new edge to the graph connecting 'n1' and 'n2'.

        'n1' points to 'n2'

        If either n1 or n2 are not already present in the graph,
        they should be added.
        """
        pass

    def del_node(self, n):
        """Delete the node 'n' from the graph.

        Raises an error if no such node exists.
        """
        pass

    def del_edge(self, n1, n2):
        """Delete the edge connecting 'n1' and 'n2' from the graph.

        Raises an error if no such edge exists.
        """
        pass

    def has_node(self, n):
        """Return True if node 'n' is contained in the graph."""
        pass

    def neighbors(self, n):
        """Return the list of all nodes connected to 'n' by edges.

        'n' points to its neighbors

        Raises an error if 'n' is not in the graph.
        """
        pass

    def adjacent(self, n1, n2):
        """Return True if there is an edge connecting 'n1' and 'n2'.

        'n1' points to 'n2'

        Raises an error if either of the supplied nodes are not in the graph.
        """
        pass
