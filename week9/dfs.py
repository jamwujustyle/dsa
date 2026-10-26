"""Zhamshid Abdulazizov, student ID 4263145."""


class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def empty(self):
        return not self.data


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"],
}


def dfs(graph, start):
    stack = Stack()
    stack.push(start)
    visited = set()
    order = []

    while not stack.empty():
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.push(neighbour)

    return order


if __name__ == "__main__":
    print("DFS order from A:", " ".join(dfs(graph, "A")))
    print("DFS order from G:", " ".join(dfs(graph, "G")))
