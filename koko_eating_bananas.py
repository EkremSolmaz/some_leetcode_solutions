import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = -1
        left = 1
        right = max(piles)

        while right >= left:
            mid = (right+left) // 2

            hours_needed = 0
            for p in piles:
                hours_needed += math.ceil(p / mid)

            if hours_needed > h:
                left = mid + 1
            else:
                res = mid
                right = mid - 1

        return res

# 0, 30 -> 15 -> 8 > 5
# 16, 30 -> 23 -> 6 > 5
# 24, 30 -> 27 -> 6 > 5
# 28, 30 -> 29 -> 6 > 5
# 30, 30

# 0, 11 -> 5 -> 7 < 8
# 0, 4 -> 2 -> 15 > 8
# 3, 4 -> 3 -> 10 > 8
# 4, 4 ->


print(Solution().minEatingSpeed([3, 6, 7, 11], 8))
print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 5))
print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 6))
print(Solution().minEatingSpeed([312884470], 312884469))
# assert Solution().minEatingSpeed([3, 6, 7, 11], 8) == 4
# assert Solution().minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
# assert Solution().minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
