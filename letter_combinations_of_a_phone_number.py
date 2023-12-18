

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        
        res = []
        for d in digits:
                if len(res) < 1:
                    for c in mapping[d]:
                        res.append(c)
                else:
                    new_res = []
                    for r in res:
                        for c in mapping[d]:
                            new_res.append(r + c)
                    res = new_res

        return new_res


        return res



print("Expected: ",  ["ad","ae","af","bd","be","bf","cd","ce","cf"])
print(Solution().letterCombinations(digits = "23"))