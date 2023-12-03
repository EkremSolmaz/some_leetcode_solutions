class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        stars = 0
        for x in s:
            if x == '*':
                res.pop(-1)
            else:
                res.append(x)

        return "".join(res)
    
print("Expected: 'lecoe', Result:", Solution().removeStars("leet**cod*e"))
print("Expected: '', Result:", Solution().removeStars("erase*****"))