from typing import List


def nmin(nums: List[int], c: int) -> int:
    if not all(type(t) is int for t in nums):
        raise TypeError

    n = len(nums)
    if n < 3:
        return None

    nums.sort()
    first, last = nums[0], nums[0]
    for i in range(1, c):
        first *= nums[i]
        last *= nums[n-i]

    return min(first, last)
