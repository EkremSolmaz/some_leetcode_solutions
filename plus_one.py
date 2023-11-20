from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1

        if i > -1:
            digits[i] += 1
            return digits
        else:
            return [1] + digits

    def plusOne2(self, digits: List[int]) -> List[int]:
        # another way of doing

        if digits == []:
            return [1]
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        return self.plusOne(digits[:-1]) + [0]


s = Solution()
print(s.plusOne([9, 9, 9, 9, 9, 9, 9]))
print(s.plusOne2([9, 9, 9, 9, 9, 9, 9]))
