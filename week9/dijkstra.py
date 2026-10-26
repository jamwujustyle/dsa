"""Zhamshid Abdulazizov, student ID 4263145."""


graph = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "E": 2, "F": 6},
    "E": {"C": 10, "D": 2, "F": 3},
    "F": {"D": 6, "E": 3},
}


def print_distances(label, dist):
    values = []
    for node in sorted(dist):
        value = "INF" if dist[node] == float("inf") else str(dist[node])
        values.append(f"{node}={value}")
    print(f"{label:<13} | " + " ".join(values))


def dijkstra(graph, source, trace=False):
    dist = {}
    prev = {}
    for node in graph:
        dist[node] = float("inf")
        prev[node] = None
    dist[source] = 0
    settled = set()

    if trace:
        print_distances("init", dist)

    while True:
        node = None
        for candidate in sorted(graph):
            if candidate not in settled:
                if node is None or dist[candidate] < dist[node]:
                    node = candidate
        if node is None or dist[node] == float("inf"):
            break

        settled.add(node)
        for neighbour in sorted(graph[node]):
            if neighbour not in settled:
                cost = dist[node] + graph[node][neighbour]
                if cost < dist[neighbour]:
                    dist[neighbour] = cost
                    prev[neighbour] = node

        if trace:
            print_distances(f"settle {node} ({dist[node]})", dist)

    return dist, prev


def get_path(prev, source, target):
    path = []
    while target is not None:
        path.append(target)
        if target == source:
            path.reverse()
            return path
        target = prev[target]
    return []


if __name__ == "__main__":
    source = "A"
    dist, prev = dijkstra(graph, source, trace=True)
    for target in sorted(graph):
        if target == source:
            continue
        path = get_path(prev, source, target)
        if not path:
            print(f"{source} to {target}: no path")
        else:
            print(f"{source} to {target}: cost {dist[target]}: "
                  + " -> ".join(path))
