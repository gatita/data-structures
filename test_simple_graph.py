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
