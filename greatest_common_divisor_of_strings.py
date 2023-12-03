class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = ""
        for i in range(len(str1)):
            prefix = str1[:i+1]
            if str1 == (len(str1) // len(prefix)) * prefix and str2 == (len(str2) // len(prefix)) * prefix:
                gcd = prefix


        return gcd
    
s = Solution()
# print( s.gcdOfStrings(str1 = "ABCABC", str2 = "ABC") ,"ABC")
print( s.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB") ,"AB")
# print( s.gcdOfStrings(str1 = "LEET", str2 = "CODE") , "")