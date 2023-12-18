from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for i in range(len(intervals)-1):
            inter = intervals[i]
            next_inter = intervals[i+1]

            if next_inter[0] <= inter[1]:
                next_inter[1] = max(next_inter[1], inter[1])
                next_inter[0] = inter[0]
            else:
                res.append(inter)

        res.append(intervals[-1])
            
        return res
    

print(Solution().merge( [[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge( [[1,3],[3,5]]))
print(Solution().merge( [[1,3],[7,5]]))
print(Solution().merge( [[1,2]]))
print(Solution().merge( [[5,7],[2,2]]))
print(Solution().merge( [[1,7],[2,2]]))
