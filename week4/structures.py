"""Week 4 (2026-09-14): Stacks, queues, and linked lists."""


from collections import deque


class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def empty(self):
        return not self.data


class Queue:
    def __init__(self):
        self.data = deque()

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.popleft()

    def empty(self):
        return not self.data


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, value):
        self.head = Node(value, self.head)

    def find(self, value):
        current = self.head
        while current is not None:
            if current.val == value:
                return current
            current = current.next
        return None

    def pop_front(self):
        if self.head is None:
            raise IndexError("list is empty")
        value = self.head.val
        self.head = self.head.next
        return value


if __name__ == "__main__":
    stack = Stack()
    queue = Queue()
    linked = LinkedList()
    for value in (1, 2, 3):
        stack.push(value)
        queue.enqueue(value)
        linked.push_front(value)
    print("Stack:", stack.pop())
    print("Queue:", queue.dequeue())
    print("Linked list:", linked.pop_front())
    print("Found:", linked.find(2).val)
