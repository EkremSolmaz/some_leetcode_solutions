def is_anagram(str1, str2):
    counter = {}

    for c in str1:
        counter[c] = counter.get(c, 0) + 1

    for c in str2:
        if c in counter.keys():
            counter[c] -= 1
        else: 
            return False

    return not any(counter.values())

assert is_anagram("listen", "silent") == True
assert is_anagram("hello", "world") == False
assert is_anagram("raceeee", "care") == False
assert is_anagram("python", "typhon") == True
assert is_anagram("apple", "orange") == False
assert is_anagram("moon", "mood") == False
assert is_anagram("heart", "earth") == True
assert is_anagram("stop", "tops") == True
assert is_anagram("lamp", "maple") == False
assert is_anagram("coding", "dingoc") == True
