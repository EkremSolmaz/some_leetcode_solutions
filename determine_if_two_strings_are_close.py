class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n, m = len(word1), len(word2)
        if n != m or set(word1) != set(word2):
            return False

        d1 = {}
        d2 = {}
        for i in range(n):
            d1[word1[i]] = d1.get(word1[i], 0) + 1
            d2[word2[i]] = d2.get(word2[i], 0) + 1

        return sorted(d1.values()) == sorted(d2.values())


print("Expected: true, got:", Solution().closeStrings(word1="abc", word2="bca"))
print("Expected: false, got:", Solution().closeStrings(word1="a", word2="aa"))
print("Expected: true, got:", Solution().closeStrings(
    word1="cabbba", word2="abbccc"))

print("Expected: false, got:", Solution().closeStrings(
    word1="cabbba", word2="aabbss"))
