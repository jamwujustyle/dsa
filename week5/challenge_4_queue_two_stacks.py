"""Week 5 (2026-09-21): Challenge 4 — Queue using two linked stacks."""


class _Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class _LinkedStack:
    """Stack with O(1) push/pop and linked nodes as its only storage."""

    def __init__(self):
        self._head = None

    def push(self, value):
        self._head = _Node(value, self._head)

    def pop(self):
        if self._head is None:
            raise IndexError("stack is empty")
        value = self._head.value
        self._head = self._head.next
        return value

    def empty(self):
        return self._head is None


# Time: enqueue O(1), dequeue amortized O(1) / worst O(n); total space: O(n).
class Queue:
    def __init__(self):
        self.incoming = _LinkedStack()
        self.outgoing = _LinkedStack()

    def enqueue(self, value):
        self.incoming.push(value)

    def dequeue(self):
        if self.outgoing.empty():
            while not self.incoming.empty():
                self.outgoing.push(self.incoming.pop())
        if self.outgoing.empty():
            raise IndexError("queue is empty")
        return self.outgoing.pop()

    def empty(self):
        return self.incoming.empty() and self.outgoing.empty()


if __name__ == "__main__":
    queue = Queue()
    for value in (1, 2, 3):
        queue.enqueue(value)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.empty()

    queue.enqueue(10)
    queue.enqueue(20)
    assert queue.dequeue() == 10
    queue.enqueue(30)
    assert queue.dequeue() == 20
    assert queue.dequeue() == 30
    assert queue.empty()

    try:
        queue.dequeue()
    except IndexError as error:
        assert str(error) == "queue is empty"
    else:
        raise AssertionError("An empty queue must raise IndexError")
    print("Challenge 4: all tests passed.")
