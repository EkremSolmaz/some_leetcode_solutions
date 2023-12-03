class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
            else:

                word = ""
                while stack[-1] != '[':
                    word = stack.pop() + word
                stack.pop() # pop [

                num_str = ""
                while len(stack) > 0 and stack[-1] in "0123456789":
                    num_str = stack.pop() + num_str

                stack.append(int(num_str) * word) 

        return "".join(stack)

print("Expected: aaabcbc, Result:",Solution().decodeString(s = "3[a]2[bc]"))
print("Expected: accaccacc, Result:",Solution().decodeString(s = "3[a2[c]]"))
print("Expected: abcabccdcdcdef, Result:",Solution().decodeString(s = "2[abc]3[cd]ef"))