import pytest
from simple_graph import SimpleGraph


@pytest.fixture
def make_graph_three():
    my_graph = SimpleGraph()
    my_graph.add_node('a')
    my_graph.add_node('b')
    my_graph.add_node('c')
    my_graph.add_edge('a', 'c')
    my_graph.add_edge('b', 'a')
    return my_graph


@pytest.fixture
def make_graph_no_edges():
    my_graph = SimpleGraph()
    my_graph.add_node('a')
    my_graph.add_node('b')
    my_graph.add_node('c')
    return my_graph


@pytest.fixture
def make_graph_empty():
    return SimpleGraph()


@pytest.fixture
def make_graph_big():
    my_graph = SimpleGraph()
    my_graph.add_node('a')
    my_graph.add_node('b')
    my_graph.add_node('c')
    my_graph.add_node('d')
    my_graph.add_edge('a', 'c')
    my_graph.add_edge('b', 'a')
    my_graph.add_edge('a', 'b')
    my_graph.add_edge('a', 'd')
    my_graph.add_edge('b', 'd')
    return my_graph


@pytest.fixture
def make_graph():
    g = SimpleGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('c', 'f')
    g.add_edge('g', 'f')
    g.add_edge('a', 'd')
    g.add_edge('d', 'e')
    g.add_edge('e', 'a')
    return g


@pytest.fixture
def make_graph_cycle():
    g = SimpleGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('c', 'a')
    return g


def test_nodes(make_graph_three):
    my_graph = make_graph_three
    nodes = sorted(my_graph.nodes())
    assert nodes == ['a', 'b', 'c']


def test_edges(make_graph_three):
    my_graph = make_graph_three
    edges = my_graph.edges()
    edges.sort(key=lambda tup: tup[0])
    assert edges == [('a', 'c'), ('b', 'a')]


def test_add_node_empty(make_graph_empty):
    my_graph = make_graph_empty
    my_graph.add_node('a')
    assert 'a' in my_graph.graph


def test_add_node(make_graph_three):
    my_graph = make_graph_three
    my_graph.add_node('d')
    assert 'd' in my_graph.graph


def test_add_edge_empty(make_graph_empty):
    my_graph = make_graph_empty
    my_graph.add_edge('a', 'b')
    assert 'a' in my_graph.graph
    assert 'b' in my_graph.graph
    assert my_graph.graph['a'] == ['b']


def test_add_edge_no_n2(make_graph_no_edges):
    my_graph = make_graph_no_edges
    my_graph.add_edge('a', 'z')
    assert 'a' in my_graph.graph
    assert 'z' in my_graph.graph
    assert my_graph.graph['a'] == ['z']


def test_add_edge_no_n1(make_graph_no_edges):
    my_graph = make_graph_no_edges
    my_graph.add_edge('z', 'a')
    assert 'a' in my_graph.graph
    assert 'z' in my_graph.graph
    assert my_graph.graph['z'] == ['a']


def test_add_edge(make_graph_no_edges):
    my_graph = make_graph_no_edges
    my_graph.add_edge('a', 'b')
    assert my_graph.graph['a'] == ['b']


def test_add_edge_multiples(make_graph_no_edges):
    my_graph = make_graph_no_edges
    my_graph.add_edge('a', 'b')
    my_graph.add_edge('a', 'b')
    assert my_graph.graph['a'].count('b') == 1


def test_del_node_exists(make_graph_three):
    my_graph = make_graph_three
    assert 'a' in my_graph.graph
    my_graph.del_node('a')
    assert 'a' not in my_graph.graph
    assert 'a' not in my_graph.graph['b']


def test_del_node_empty(make_graph_empty):
    my_graph = make_graph_empty
    with pytest.raises(KeyError):
        my_graph.del_node('a')


def test_del_edge_exists(make_graph_three):
    my_graph = make_graph_three
    my_graph.del_edge('a', 'c')
    assert 'c' not in my_graph.graph['a']


def test_del_edge_exists_2(make_graph_big):
    my_graph = make_graph_big
    my_graph.del_edge('a', 'c')
    assert 'c' not in my_graph.graph['a']


def test_del_edge_empty(make_graph_empty):
    my_graph = make_graph_empty
    with pytest.raises(KeyError):
        my_graph.del_edge('a', 'b')


def test_has_node(make_graph_big):
    my_graph = make_graph_big
    assert my_graph.has_node('a') is True
    assert my_graph.has_node('z') is False


def test_neighbors(make_graph_big):
    my_graph = make_graph_big
    assert my_graph.neighbors('a') == ['c', 'b', 'd']


def test_neighbors_empty(make_graph_empty):
    my_graph = make_graph_empty
    with pytest.raises(KeyError):
        my_graph.neighbors('a')


def test_adjacent_exists(make_graph_big):
    my_graph = make_graph_big
    assert my_graph.adjacent('a', 'b') is True


def test_adjacent_no_edge(make_graph_big):
    my_graph = make_graph_big
    with pytest.raises(IndexError):
        my_graph.adjacent('a', 'z')


def test_adjacent_no_node(make_graph_big):
    my_graph = make_graph_big
    with pytest.raises(IndexError):
        my_graph.adjacent('z', 'a')


def test_breadth_first_traverasal(make_graph):
    g = make_graph
    path = g.breadth_first_traversal('a')
    assert path == [u'a', u'b', u'd', u'c', u'e', u'f']


def test_depth_first_traverasal(make_graph):
    g = make_graph
    path = g.depth_first_traversal('a')
    assert path == [u'a', u'b', u'c', u'f', u'd', u'e']


def test_breadth_first_traversal_empty(make_graph_empty):
    """providing 'start' node that doesn't exists raises KeyError"""
    g = make_graph_empty
    with pytest.raises(KeyError):
        g.breadth_first_traversal('a')


def test_depth_first_traversal_empty(make_graph_empty):
    """providing 'start' node that doesn't exists raises KeyError"""
    g = make_graph_empty
    with pytest.raises(KeyError):
        g.depth_first_traversal('a')


def test_breadth_first_excluded(make_graph):
    """'g' points to 'f', but nobody points to 'g'
    so 'g' should not be in the path
    """
    g = make_graph
    path = g.breadth_first_traversal('a')
    assert 'g' not in path


def test_depth_first_excluded(make_graph):
    """'g' points to 'f', but nobody points to 'g'
    so 'g' should not be in the path
    """
    g = make_graph
    path = g.depth_first_traversal('a')
    assert 'g' not in path


def test_breadth_first_cycle(make_graph_cycle):
    g = make_graph_cycle
    path = g.breadth_first_traversal('a')
    assert path == [u'a', u'b', u'c']


def test_depth_first_cycle(make_graph_cycle):
    g = make_graph_cycle
    path = g.depth_first_traversal('a')
    assert path == [u'a', u'b', u'c']
