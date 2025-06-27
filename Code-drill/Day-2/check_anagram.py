

from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

print(isAnagram("listen", "silent"))  # True
print(isAnagram("hello", "hell"))     # False
print(isAnagram("anagram", "nagaram"))  # True
print(isAnagram("rat", "car"))          # False

