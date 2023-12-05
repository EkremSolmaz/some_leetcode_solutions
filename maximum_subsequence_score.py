from typing import List
import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        sorts = sorted(zip(nums2, nums1), reverse=True)

        multiplier = sorts[k-1][0]
        heap = [num[1] for num in sorts[:k]]
        max_so_far = 0
        total = sum(heap)

        heapq.heapify(heap)

        for num2, num1 in sorts[k:]:
            result = total * multiplier
            if (result > max_so_far):
                max_so_far = result

            multiplier = num2
            total += num1 - heapq.heappop(heap)
            heapq.heappush(heap, num1)

        result = total * multiplier
        max_so_far = max(max_so_far, result)

        return max_so_far


print(Solution().maxScore(nums1=[1, 3, 3, 2], nums2=[2, 1, 3, 4], k=3))
