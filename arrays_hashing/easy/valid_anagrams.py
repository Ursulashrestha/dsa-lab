# Valid Anagrams - An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# Input: s = "listen", t = "silent"
# Output: true
# Input: s = "rat", t = "tap"
# Output: false

# Method 1 (Using Sorting)
def isAnagram(self, s: str, t:str):
    return sorted(s) == sorted(t)
# Time Complexity = (Onlogn) = because sorting takes time
# Space Complexity = O(n) = storing the sorted list
 
# Method 2 (Using Counter)
from collections import Counter

def isAnagram(self, s:str, t:str):
# Counter(s) ---> {'r':1, 'a': 1, 't':1}
# Counter(t) ---> {'t':1, 'a': 1, 'p':1}
    return Counter(s)== Counter(t)

# Time Complexity = (On) = because it counts each letter only once
# Space Complexity = O(1) = only 26 lowercase letters

# Method 3 (Using Dictionaries/ HashMap)
# Create two different dictionries for each


