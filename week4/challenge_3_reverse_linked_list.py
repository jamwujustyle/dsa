"""Week 4 (2026-09-14): Challenge 3 — Reverse a singly linked list."""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# Time: O(n); auxiliary space: O(1), reusing the n existing nodes.
def reverse_list(head):
    previous = None
    current = head
    while current is not None:
        following = current.next
        current.next = previous
        previous = current
        current = following
    return previous


if __name__ == "__main__":
    first, second, third = Node(1), Node(2), Node(3)
    first.next, second.next = second, third
    head = reverse_list(first)
    assert head is third
    assert third.next is second and second.next is first and first.next is None

    single = Node(7)
    assert reverse_list(single) is single and single.next is None

    assert reverse_list(None) is None
    print("Challenge 3: all tests passed.")
