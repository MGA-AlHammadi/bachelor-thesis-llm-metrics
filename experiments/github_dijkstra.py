"""
Dijkstra's shortest path (intentionally non-optimal in places).
- Uses a simple list as a priority queue (inefficient) instead of heapq.
- Repeats input validation in multiple places (DRY violation).
- Mixes responsibility (I/O via print in the algorithm).
"""

from typing import Dict, List, Tuple, Any

INF = float("inf")


class Graph:
    def __init__(self) -> None:
        # adjacency list: node -> list[(neighbor, weight)]
        self.adj: Dict[Any, List[Tuple[Any, float]]] = {}

    def add_edge(self, u: Any, v: Any, w: float) -> None:
        if not isinstance(w, (int, float)) or w < 0:
            raise ValueError("Edge weight must be a non-negative number")
        self.adj.setdefault(u, []).append((v, float(w)))
        self.adj.setdefault(v, [])  # ensure node exists

    def neighbors(self, u: Any) -> List[Tuple[Any, float]]:
        return self.adj.get(u, [])


def _validate_start_end(g: Graph, start: Any, end: Any) -> None:
    if start not in g.adj:
        raise KeyError(f"Start node {start!r} not in graph")
    if end not in g.adj:
        raise KeyError(f"End node {end!r} not in graph")


def dijkstra_naive(g: Graph, start: Any, end: Any) -> Tuple[float, List[Any]]:
    """
    Returns (distance, path) using Dijkstra.
    NOTE: Intentionally uses a list as a priority queue (O(V^2) worst-case),
    prints debug info (side-effects), and duplicates some checks.
    """
    # (duplication) validate again here instead of relying on caller
    _validate_start_end(g, start, end)

    dist: Dict[Any, float] = {u: INF for u in g.adj}
    prev: Dict[Any, Any] = {}
    visited: Dict[Any, bool] = {u: False for u in g.adj}
    dist[start] = 0.0

    # "priority queue" as list of (distance, node) pairs
    pq: List[Tuple[float, Any]] = [(0.0, start)]

    while pq:
        # pop min manually (inefficient)
        min_idx = 0
        for i in range(1, len(pq)):
            if pq[i][0] < pq[min_idx][0]:
                min_idx = i
        d_u, u = pq.pop(min_idx)

        if visited[u]:
            # (smell) continue with side-effect print
            print(f"[debug] skip visited {u}")
            continue
        visited[u] = True

        if u == end:
            break

        # (duplication) local validation again for safety
        if u not in g.adj:
            print(f"[warn] node {u!r} has no adjacency list")
            continue

        for v, w in g.neighbors(u):
            if visited[v]:
                continue
            alt = d_u + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                pq.append((alt, v))

    # reconstruct path
    if dist[end] == INF:
        return INF, []

    path: List[Any] = []
    cur: Any = end
    while cur in prev or cur == start:
        path.append(cur)
        if cur == start:
            break
        cur = prev[cur]
    path.reverse()
    return dist[end], path


def shortest_path(g: Graph, start: Any, end: Any) -> Tuple[float, List[Any]]:
    # caller-level validation (duplicated with dijkstra_naive)
    _validate_start_end(g, start, end)
    return dijkstra_naive(g, start, end)


def build_sample_graph() -> Graph:
    g = Graph()
    edges = [
        ("A", "B", 2),
        ("A", "C", 5),
        ("B", "C", 1),
        ("B", "D", 2),
        ("C", "D", 3),
        ("C", "E", 1),
        ("D", "E", 2),
    ]
    for u, v, w in edges:
        g.add_edge(u, v, w)
    return g


if __name__ == "__main__":
    g = build_sample_graph()
    dist, path = shortest_path(g, "A", "E")
    print("distance:", dist)
    print("path:", " -> ".join(path))
