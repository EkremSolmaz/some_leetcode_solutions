from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        op = 0
        while matrix:
            if op == 0:
                res += matrix[0]
                matrix = matrix[1:]

            elif op == 1:
                res += [row[-1] for row in matrix if row]
                matrix = [row[:-1] for row in matrix]

            elif op == 2:
                res += list(reversed(matrix[-1]))
                matrix = matrix[:-1]

            elif op == 3:
                res += list(reversed([row[0] for row in matrix if row]))
                matrix = [row[1:] for row in matrix]

            op += 1
            op %= 4


        return res
    
print(Solution().spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(Solution().spiralOrder(matrix =[[7],[9],[6]]))
print(Solution().spiralOrder(matrix =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))

"""
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16
"""