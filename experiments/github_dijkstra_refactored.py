"""
Refactored version of the Dijkstra algorithm.
Implements clean architecture, better data structures, and improved readability.
"""

import heapq
from typing import Dict, List, Tuple, TypeVar, Generic, Optional

T = TypeVar("T")
INF = float("inf")


class Graph(Generic[T]):
    """Simple directed weighted graph using adjacency lists."""

    def __init__(self) -> None:
        """Initialize an empty adjacency list."""
        self.adj: Dict[T, List[Tuple[T, float]]] = {}

    def add_edge(self, u: T, v: T, w: float) -> None:
        """
        Add a directed edge (u -> v) with weight w.

        Args:
            u: Start node
            v: End node
            w: Edge weight (must be non-negative)
        Raises:
            ValueError: If weight is negative or invalid.
        """
        if not isinstance(w, (int, float)):
            raise ValueError("Edge weight must be numeric")
        if w < 0:
            raise ValueError("Edge weight must be non-negative")

        self.adj.setdefault(u, []).append((v, float(w)))
        self.adj.setdefault(v, [])  # Ensure the node exists in the graph

    def neighbors(self, u: T) -> List[Tuple[T, float]]:
        """Return a list of neighbors for node u."""
        return self.adj.get(u, [])


def validate_nodes(g: Graph[T], start: T, end: T) -> None:
    """
    Validate that both start and end nodes exist in the graph.
    """
    if start not in g.adj:
        raise KeyError(f"Start node {start!r} not found in graph")
    if end not in g.adj:
        raise KeyError(f"End node {end!r} not found in graph")


def dijkstra_heapq(g: Graph[T], start: T, end: T) -> Tuple[float, List[T]]:
    """
    Compute the shortest path between two nodes using Dijkstra’s algorithm.

    Args:
        g: Graph instance
        start: Start node
        end: End node

    Returns:
        A tuple (distance, path)
        - distance: total distance from start to end
        - path: list of nodes in the shortest path

    Raises:
        KeyError: If start or end node not found.
    """
    validate_nodes(g, start, end)

    dist: Dict[T, float] = {u: INF for u in g.adj}
    prev: Dict[T, Optional[T]] = {}
    dist[start] = 0.0

    pq: List[Tuple[float, T]] = [(0.0, start)]
    visited: set[T] = set()

    while pq:
        d_u, u = heapq.heappop(pq)

        if u in visited:
            continue

        visited.add(u)

        if u == end:
            break

        for v, weight in g.neighbors(u):
            if v in visited:
                continue

            alt = d_u + weight
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(pq, (alt, v))

    if dist[end] == INF:
        return INF, []

    path: List[T] = []
    cur: Optional[T] = end
    max_depth = len(g.adj)

    while cur is not None and len(path) <= max_depth:
        path.append(cur)
        if cur == start:
            break
        cur = prev.get(cur)

    if not path or path[-1] != start:
        return INF, []

    path.reverse()
    return dist[end], path


def build_sample_graph() -> Graph[str]:
    """Builds a small sample graph for testing purposes."""
    g = Graph[str]()
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "C", 1)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 8)
    g.add_edge("C", "E", 10)
    g.add_edge("D", "E", 2)
    g.add_edge("E", "F", 3)
    return g


def main() -> None:
    """Test function for Dijkstra’s algorithm."""
    g = build_sample_graph()
    start, end = "A", "F"
    distance, path = dijkstra_heapq(g, start, end)
    print(f"Shortest path from {start} to {end}: {path}, distance = {distance}")


if __name__ == "__main__":
    main()
