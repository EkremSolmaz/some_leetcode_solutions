from typing import List

# Not the best solution, I know
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n,m = len(nums1), len(nums2)
        needed_on_left = (n+m) // 2 if (n+m) % 2 else (n+m) // 2 - 1
        i, j = 0, 0

        while i+j < needed_on_left and j < m and i < n:
            if nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        
        if i == n:
            return nums2[needed_on_left - i] if (n+m) % 2 else (nums2[needed_on_left - i] + nums2[needed_on_left - i + 1]) / 2
        if j == m:
            return nums1[needed_on_left - j] if (n+m) % 2 else (nums1[needed_on_left - j] + nums1[needed_on_left - j + 1]) / 2
        
        if (n+m) % 2:
            return min(nums1[i], nums2[j])
        
        if nums1[i] < nums2[j]:
            min1 = nums1[i]
            i += 1
            min2 = min(nums1[i], nums2[j]) if i < n else nums2[j]
        else:
            min1 = nums2[j]
            j += 1
            min2 = min(nums1[i], nums2[j]) if j < m else nums1[i]

        return (min1 + min2) / 2




print("Expected: 4, Result: ", Solution().findMedianSortedArrays(nums1 = [1,2,3,4], nums2 = [1,4,5,6,9]))
print("Expected: 2.5, Result: ", Solution().findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))