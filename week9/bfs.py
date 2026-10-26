"""Zhamshid Abdulazizov, student ID 4263145."""


class Queue:
    def __init__(self):
        self.data = []
        self.front = 0

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        value = self.data[self.front]
        self.front += 1
        return value

    def empty(self):
        return self.front == len(self.data)


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"],
}


def bfs(graph, start):
    queue = Queue()
    queue.enqueue(start)
    dist = {start: 0}
    parent = {start: None}
    order = []

    while not queue.empty():
        node = queue.dequeue()
        order.append(node)
        for neighbour in graph[node]:
            if neighbour not in dist:
                dist[neighbour] = dist[node] + 1
                parent[neighbour] = node
                queue.enqueue(neighbour)

    return order, dist, parent


def get_path(parent, target):
    if target not in parent:
        return []
    path = []
    while target is not None:
        path.append(target)
        target = parent[target]
    path.reverse()
    return path


def print_shortest(graph, start, target):
    order, dist, parent = bfs(graph, start)
    path = get_path(parent, target)
    if not path:
        print(f"Shortest {start} -> {target}: no path")
    else:
        print(f"Shortest {start} -> {target}: distance {dist[target]}, path "
              + " -> ".join(path))


if __name__ == "__main__":
    order, dist, parent = bfs(graph, "A")
    print("BFS order from A:", " ".join(order))
    print_shortest(graph, "A", "G")
    print_shortest(graph, "D", "G")
