from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return ' '.join(words)
    

s = Solution()
print("|",s.reverseWords("the sky is blue"),"|")
print("|",s.reverseWords(" the sky is blue "),"|")
print("|",s.reverseWords(" "),"|")
