from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        thresh = max(candies) - extraCandies
        return [c  >= thresh for c in candies]