from typing import List


class Solution:
    def combSum(self, candidates, target, path = []):
        cnt = 0
        paths = []
        for i in range(len(candidates)):
            c = candidates[i]
            if c == target:
                paths.append(path + [c])
                cnt += 1
            elif c < target:
                paths += self.combSum(candidates[i:], target - c, path + [c])
        return paths


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.combSum(candidates, target)


print(Solution().combinationSum(candidates = [2,3,6,7], target = 7))
print(Solution().combinationSum(candidates = [2,3,5], target = 8))
print(Solution().combinationSum(candidates = [2], target = 1))
