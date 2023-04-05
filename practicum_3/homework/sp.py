from typing import Any
import queue

import networkx as nx

from src.plotting import plot_graph


def dijkstra_sp(G: nx.Graph, source_node="0") -> dict[Any, list[Any]]:
    shortest_paths = {}  # key = destination node, value = list of intermediate nodes

    pq = queue.PriorityQueue()
    dist = {node: float("inf") for node in G.nodes()}
    dist[source_node] = 0

    pq.put((0, source_node))

    while not pq.empty():
        current_dist, current_node = pq.get()
        if current_dist > dist[current_node]:
            continue

        for neighbor, attr in G[current_node].items():
            new_dist = dist[current_node] + attr["weight"]
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                pq.put((new_dist, neighbor))

        shortest_paths[current_node] = [source_node]
        node = current_node
        while node != source_node:
            prev_node = min(G[node], key=lambda x: dist[x] + G[node][x]["weight"])
            shortest_paths[current_node].append(prev_node)
            node = prev_node
        shortest_paths[current_node].reverse()

    return shortest_paths


if __name__ == "__main__":
    G = nx.read_edgelist("graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    shortest_paths = dijkstra_sp(G, source_node="0")
    test_node = "5"
    shortest_path_edges = [
        (shortest_paths[test_node][i], shortest_paths[test_node][i + 1])
        for i in range(len(shortest_paths[test_node]) - 1)
    ]
    plot_graph(G, highlighted_edges=shortest_path_edges)
