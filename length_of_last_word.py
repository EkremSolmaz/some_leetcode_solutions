class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n-1, -1, -1):
            if s[i] == ' ':
                if res != 0:
                    return res
                continue
            res += 1
            
        return res
            
    
    
        
s = Solution()
print(s.lengthOfLastWord( "a"))