from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = r = 0
        res = 0
        zeros = 0
        for r, numr in enumerate(nums):
            if numr == 0:
                zeros += 1
            
            while zeros > 1 and l < len(nums):
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            
            if zeros < 2:
                res = max(res, r-l)
                
        return res - 1 if res == len(nums) else res
                
                



print("Expected 5, Result:", Solution().longestSubarray([0,1,1,1,0,1,1,0,1]))
print("Expected 4, Result:", Solution().longestSubarray([1,1,0,0,1,1,1,0,1]))
print("Expected 3, Result:", Solution().longestSubarray([1,1,0,1]))
print("Expected 2, Result:", Solution().longestSubarray([1,1,1]))