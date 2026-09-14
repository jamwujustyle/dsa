"""Week 4 (2026-09-14): Challenge 1 — Balanced brackets."""


# Time: O(n); auxiliary space: O(n), for n input characters.
def balanced_brackets(text):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack


if __name__ == "__main__":
    assert balanced_brackets("(a[b]{c})")
    assert not balanced_brackets("([)]")
    assert balanced_brackets("")
    assert not balanced_brackets("]")
    assert not balanced_brackets("((")
    print("Challenge 1: all tests passed.")
