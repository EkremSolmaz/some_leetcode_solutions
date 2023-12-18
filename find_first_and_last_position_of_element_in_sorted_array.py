from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.search(nums, target)
    
    def search(self, nums, target):
        if not nums:
            return [-1,-1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            return [-1,-1]
        mid = len(nums) // 2
        l,r = nums[:mid], nums[mid:]
        if nums[mid] == target:
            l_res = self.search(l, target)[0]
            r_res = self.search(r, target)[1]
            l_res = mid if l_res == -1 else l_res
            r_res = mid if r_res == -1 else r_res
            return [l_res, r_res+mid]
        if nums[mid] > target:
            return self.search(l, target)
        elif nums[mid] < target:
            return [x if x == -1 else x+mid for x in self.search(r, target)]
        



"""
5,5,5,7,8,9,9,9 -> 5

"""

print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 8))
print(Solution().searchRange(nums = [5,7,7,8,8,8,8,10], target = 8))
print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 5))
print(Solution().searchRange(nums = [7,7,8,8,10], target = 5))
print(Solution().searchRange(nums = [], target = 5))