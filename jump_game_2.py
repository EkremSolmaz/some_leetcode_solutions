from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        target = len(nums) - 1
        cnt = 0
        while target > 0:
            for i, x in enumerate(nums):
                if x >= (target - i):
                    target = i
                    break

            cnt += 1

        return cnt


print(Solution().jump([3, 2, 1]))
print(Solution().jump([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(Solution().jump([1, 2, 1, 1, 1]))
print(Solution().jump([2, 3, 1, 1, 4]))
print(Solution().jump([2, 3, 0, 1, 4]))
print(Solution().jump([1, 2, 3]))
print(Solution().jump([]))
print(Solution().jump([2, 0, 2]))
