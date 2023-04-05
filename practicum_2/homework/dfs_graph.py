from queue import LifoQueue
from typing import Any

import networkx as nx

from src.plotting import plot_graph


def visit(node: Any):
    print(f"Wow, it is {node} right here!")


def dfs_iterative(G: nx.Graph, node: Any):
    visited = {n: False for n in G}
    visited[node] = True

    lifo_queue = LifoQueue()
    lifo_queue.put(node)

    while not lifo_queue.empty():
        curr_node = lifo_queue.get()
        visited[curr_node] = True
        visit(curr_node)

        for neighbor in G.neighbors(curr_node):
            if not visited[neighbor]:
                lifo_queue.put(neighbor)


def recursive_dfs(G: nx.DiGraph, node: Any, visited: set, lifo_queue: LifoQueue):
    visited[node] = True

    for neighbor in G.neighbors(node):
        if not visited[neighbor]:
            recursive_dfs(G, neighbor, visited, lifo_queue)

    lifo_queue.put(node)
def topological_sort(G: nx.DiGraph, node: Any):
    visited = {n: False for n in G}

    lifo_queue = LifoQueue()
    recursive_dfs(G, node, visited, lifo_queue)

    while not lifo_queue.empty():
        curr_node = lifo_queue.get()
        visit(curr_node)


if __name__ == "__main__":
    # Load and plot the graph
    G = nx.read_edgelist("graph_2.edgelist", create_using=nx.Graph)
    # plot_graph(G)

    print("Iterative DFS")
    print("-" * 32)
    dfs_iterative(G, node="0")
    print()

    G = nx.read_edgelist(
        "graph_2.edgelist", create_using=nx.DiGraph
)
    plot_graph(G)
    print("Topological sort")
    print("-" * 32)
    topological_sort(G, node="0")
