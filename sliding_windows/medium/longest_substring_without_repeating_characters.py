#Longest Substring without repeating character
strs = 'abcabcbb'
#output = 3
def longestlengthSubstring(strs:str)-> int:
    mp = {} #stores the last place the letter was found
    l = 0
    res = 0
    for r in range(len(strs)):
        if strs[r] in mp: #if number is found in mp
            l = max(mp[strs[r]]+1,l) #move l skipping the previous/old char and make sure it doesnt move backward
        mp[strs[r]]= r #update the index in mp for repeated char
        res = max(res, r-l+1)
    return res
#Time complexity: O(n)
#Space complexity: O(m)