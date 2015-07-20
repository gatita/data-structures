# data-structures [![Build Status](https://travis-ci.org/wilson0xb4/data-structures.svg?branch=master)](https://travis-ci.org/wilson0xb4/data-structures)
Sample code for a number of classic data structures implemented in Python



## Queue
A container to hold nodes in a first in first out order.

## Doubly Linked List
A container of nodes that maintain links to a previous and a next node.
A doubly linked list is better to use in situations where you would want to traverse a list backwards.

#### Implemented:
* insert(val) will insert the value 'val' at the head of the list
* append(val) will append the value 'val' at the tail of the list
* pop() will pop the first value off the head of the list and return it.
* shift() will remove the last value from the tail of the list and return it.
* remove(val) will remove the first instance of 'val' found in the list, starting from the head. If 'val' is not present, it will raise an appropriate Python exception.

## Binary Heap

## Simple Graph
* g.nodes(): return a list of all nodes in the graph
* g.edges(): return a list of all edges in the graph
* g.add_node(n): adds a new node 'n' to the graph
* g.add_edge(n1, n2): adds a new edge to the graph connecting 'n1' and 'n2', if either n1 or n2 are not already present in the graph, they should be added.
* g.del_node(n): deletes the node 'n' from the graph, raises an error if no such node exists
* g.del_edge(n1, n2): deletes the edge connecting 'n1' and 'n2' from the graph, raises an error if no such edge exists
* g.has_node(n): True if node 'n' is contained in the graph, False if not.
* g.neighbors(n): returns the list of all nodes connected to 'n' by edges, raises an error if n is not in g
* g.adjacent(n1, n2): returns True if there is an edge connecting n1 and n2, False if not, raises an error if either of the supplied nodes are not in g


## Weighted Graph
Extends Simple Graph to allow for weighted edges.


### Collaborators
* Andrew
* Grace
