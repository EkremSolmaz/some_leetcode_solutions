from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1, num2 = 2 ** 31, 2 ** 31
        for n in nums:
            if n <= num1:
                num1 = n
            elif n <= num2:
                num2 = n
            else:
                return True
            
        return False

        

s = Solution()
res = s.increasingTriplet(nums = [2,1,5,0,4,6])
print(res)