import pytest

from graph.node import Node
from graph.construct import Graph
from graph.traversals import dfs, bfs

from random import seed, sample

def get_simple_graph():
    b = Node(3)
    c = Node(4, [b])
    d = Node(2)
    a = Node(1, [c, d])    
    return a

def get_cycle_graph():
    a = Node(1)
    b = Node(2)
    c = Node(3, [b])
    d = Node(5, [c, a])
    e = Node(6, [d])
    a.add_neighbor(e)
    return e

def generate_simple_graph(num_nodes, seed_num):
    seed(seed_num)
    graph = Graph(num_nodes)
    return graph.graph

test_dfs_data = [
    (get_simple_graph(), [1, 4, 3, 2]),
    (get_cycle_graph(), [6, 5, 3, 2, 1]),
    (generate_simple_graph(3, 3), [7, 16, 11]),
    (generate_simple_graph(3, 10), [17, 13, 17]),
    (generate_simple_graph(3, 100), [4, 14, 23])
]

test_bfs_data = [
    (get_simple_graph(), [1, 4, 2, 3]),
    (get_cycle_graph(), [6, 5, 3, 1, 2])
]

@pytest.mark.parametrize("graph,expected", test_dfs_data)
def test_traversal(graph, expected):
    actual = [node.data for node in dfs(graph)]
    assert actual == expected 

@pytest.mark.parametrize("graph,expected", test_bfs_data)
def test_bfs_simple(graph, expected):
    actual = [node.data for node in bfs(graph)]
    assert actual == expected 
