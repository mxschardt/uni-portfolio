from typing import List


def threemin(nums: List[int]) -> int:
    if not all(isinstance(n, int) for n in nums):
        raise TypeError

    n = len(nums)
    if n < 3:
        return None

    nums.sort()
    return min(nums[n-1] * nums[n-2] * nums[0], nums[0] * nums[1] * nums[2])
