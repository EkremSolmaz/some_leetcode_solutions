from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        n = len(nums)
        first_zero = -1
        first_non_zero = -1

        while i < n:
            if nums[i] == 0 and first_zero == -1:
                first_zero = i
                first_non_zero = -1
            if nums[i] != 0 and first_non_zero == -1:
                first_non_zero = i
            if first_zero != -1 and first_non_zero != -1 and first_zero < first_non_zero:
                nums[first_zero], nums[first_non_zero] = nums[first_non_zero], nums[first_zero]
                first_non_zero = -1
                first_zero += 1
            i += 1


a = [0,1,0,3,12]
print(a)
Solution().moveZeroes(a)
print(a)
a = [0]
print(a)
Solution().moveZeroes(a)
print(a)
a = [1, 0, 1]
print(a)
Solution().moveZeroes(a)
print(a)