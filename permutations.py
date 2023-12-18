from typing import List

def getPermutes(nums):
    if len(nums) == 1:
        return [nums]
    if len(nums) == 2:
        return [nums, list(reversed(nums))]
    combs = []
    for i, x in enumerate(nums):
        for per in getPermutes(nums[:i] + nums[i+1:]):
            combs.append([x] + per)
    return combs




class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return getPermutes(nums)


print(Solution().permute([1,2,3]))
print(Solution().permute([0,1]))
print(Solution().permute([1]))