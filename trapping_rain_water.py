from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left_max, right_max = 0, 0
        left, right = 0, len(height)-1

        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    total += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    total += right_max - height[right]
                right -= 1

        return total


s = Solution()
# print(s.trap([4,2,3]))
# print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4, 2, 0, 3, 2, 5]))
