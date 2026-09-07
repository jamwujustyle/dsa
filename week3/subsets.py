"""Week 3 (2026-09-07): Enumerating subsets."""


def subsets(nums):
    result = []
    current = []

    def backtrack(i):
        if i == len(nums):
            result.append(current.copy())
            return
        backtrack(i + 1)
        current.append(nums[i])
        backtrack(i + 1)
        current.pop()

    backtrack(0)
    return result


if __name__ == "__main__":
    print(subsets([1, 2]))
