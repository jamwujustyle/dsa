"""Week 3 (2026-09-07): Subset-sum backtracking."""


def subset_sum(nums, target):
    chosen = []

    def backtrack(i, total):
        if total == target:
            return chosen.copy()
        if i == len(nums):
            return None
        chosen.append(nums[i])
        result = backtrack(i + 1, total + nums[i])
        chosen.pop()
        if result is not None:
            return result
        return backtrack(i + 1, total)

    return backtrack(0, 0)


if __name__ == "__main__":
    print("Subset sum:", subset_sum([2, 3, 4, 8], 6))
