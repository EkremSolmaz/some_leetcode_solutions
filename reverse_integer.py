class Solution:
    def reverse(self, x: int) -> int:
        isNeg = x < 0


        max_s = str(2 ** 31 - 1)
        if isNeg:
            s = str(x)[1:]
            s = "".join(reversed(s))
            s = (len(max_s) - len(s)) * "0" + s
            print(s, max_s)
            if s > max_s:
                return 0
            return -int(s)
        else:
            s = str(x)
            s = "".join(reversed(s))
            s = (len(max_s) - len(s)) * "0" + s
            print(s, max_s)
            if s > max_s:
                return 0
            return int(s)
