class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2:
            return x
        left = 0
        right = x

        while left < right-1:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            if square < x:
                left = mid
            else:
                right = mid

        return left


s = Solution()
print(s.mySqrt(8))
