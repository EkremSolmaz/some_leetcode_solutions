from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        needs = {}
        res = 0

        for i,n in enumerate(nums):
            if needs.get(n, 0) > 0:
                res += 1
                needs[n] -= 1
            else:
                needs[k-n] = needs.get(k-n, 0) + 1

        return res


print(Solution().maxOperations(nums = [1,2,3,4], k = 5))
print(Solution().maxOperations(nums = [3,1,3,4,3], k = 6))