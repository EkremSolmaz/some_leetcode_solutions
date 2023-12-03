from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i in range(len(nums)):
            need = target - nums[i]
            if need in visited.keys():
                return [i, visited[need]]
            visited[nums[i]] = i
    

s = Solution()
print("[0,1] -> ", s.twoSum(nums = [2,7,11,15], target = 9))