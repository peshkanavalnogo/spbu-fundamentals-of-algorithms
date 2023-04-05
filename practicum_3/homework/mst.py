from typing import Any
import heapq

import matplotlib.pyplot as plt
import networkx as nx

from src.plotting import plot_graph


def prim_mst(G: nx.Graph, start_node="0") -> set[tuple[Any, Any]]:
    mst_set = set()  # set of nodes included into MST
    rest_set = set(G.nodes())  # set of nodes not yet included into MST
    mst_edges = set()  # set of edges constituting MST

    heap = []

    mst_set.add(start_node)
    rest_set.remove(start_node)

    for neighbor in G.neighbors(start_node):
        heapq.heappush(heap, (G.edges[(start_node, neighbor)]['weight'], (start_node, neighbor)))

    while rest_set:
        weight, edge = heapq.heappop(heap)
        v = edge[1]

        if v in mst_set:
            continue

        mst_edges.add(edge)
        mst_set.add(v)
        rest_set.remove(v)

        for neighbor in G.neighbors(v):
            if neighbor in rest_set:
                heapq.heappush(heap, (G.edges[(v, neighbor)]['weight'], (v, neighbor)))

    return mst_edges


if __name__ == "__main__":
    G = nx.read_edgelist("graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    mst_edges = prim_mst(G, start_node="0")
    plot_graph(G, highlighted_edges=list(mst_edges))
