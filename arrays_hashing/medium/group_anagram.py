# Group Anagrams
# In regular dictionary {}, if key is not already in the dict, it gives keyError
# Input:
# strs = ["eat","tea", "tan","ate","nat","bat"]
# Output:
# [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    grouped = defaultdict(list) # dict where each value is a list & is key doesnt exist yet, just gives an empty list

    for word in strs:
        sorted_word = ''.join(sorted(word)) # sorted(word) -> ["e","a","t"] after .join() -> "aet"
        grouped[sorted_word].append(word)
        # grouped["aet"].append(eat)
        # RESULTS: {"aet":["eat"]}
    return list (grouped.values()) # list here because grouped.values() returns a special view object like dict_values[("eat","tea")] which cant be used as normal list

# time complexity: O(m*nlogn)
# space complexity: O(m*n)

#####------------------------------------- Second/Optimal Method------------------- ######
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    result = defaultdict(list)
    for word in strs:
        count = [0]* 26
        for letter in word:
            count[ord(letter) - ord('a')]+=1  # ord('a') = 97 => constant value in ASCII
        result[tuple(count)].append(word)  # result[(1, 0, 0, 0, 1, ..., 1)] = ["eat", "ate"]
    return list(result.values())

# Time complexity : O(m*n)
# Space complexity: O(m)


    