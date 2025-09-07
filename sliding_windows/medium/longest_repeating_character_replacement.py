# Longest Repeating Character Replaement
s = "ABAB"
k  = 2
# output = 4

s = "AABABBA", 
k = 1
#Output: 4

def characterReplacement(s:str, k:int)-> int:
    res  = 0
    count = {}
    l = 0
    maxf = 0
    for r in range(len(s)):
        count[s[r]]= 1+ count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        while (r-l+1)-maxf > k: #current size of the window - max frequency count for prohibiting more than k changes
            count[s[l]]-=1 #remove the left most char and decrease the count in dictionary
            l += 1 # move the left end of the window to the right by 1
        res = max(res, r-l+1)
    return res
#Time complexity: O(n)
#Space complexity: O(m)