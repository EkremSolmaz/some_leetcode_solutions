class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prev = self.countAndSay(n-1)
        
        res = ""
        i = 1
        last_seen=prev[0]
        counter=1
        while i < len(prev):
            if prev[i] == last_seen:
                counter += 1
            else:
                res += str(counter) + str(last_seen)
                last_seen = prev[i]
                counter = 1
            i+=1

        res += str(counter) + str(last_seen)
        return res

# print(Solution().countAndSay(4))
print(Solution().countAndSay(5))
print(Solution().countAndSay(6))