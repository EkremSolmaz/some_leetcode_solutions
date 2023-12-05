from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = sum(nums[1:])
        if l == r:
            return 0

        for pivot in range(1, n):
            l += nums[pivot-1]
            r -= nums[pivot]

            if l == r:
                return pivot

        return -1


print("Expected: 3, Result:", Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
print("Expected: -1, Result:", Solution().pivotIndex([1, 2, 3]))
print("Expected: 0, Result:", Solution().pivotIndex([2, 1, -1]))
