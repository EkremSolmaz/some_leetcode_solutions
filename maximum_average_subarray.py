from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = last_sum = sum(nums[:k])
        
        for i in range(k, len(nums)):
            last_sum += nums[i] - nums[i-k]
            if max_sum < last_sum:
                max_sum = last_sum
            
        return max_sum / k


print("Expected: 12.75, Result:", Solution().findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))
print("Expected: 5.00000, Result:", Solution().findMaxAverage(nums = [5], k = 1))
print("Expected: -1, Result:", Solution().findMaxAverage(nums = [-1], k = 1))
print("Expected: 2, Result:", Solution().findMaxAverage(nums = [0,1,1,3,3], k = 4))
