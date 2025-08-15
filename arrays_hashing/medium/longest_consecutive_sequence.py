# Longest consecutive sequence
#1 
nums = [1,2,100,3,4,200]
output = 4
#2
# nums = [0,3,2,5,4,6,1,1]
#output = 7

def longestConsecuitve(nums:list[int])-> int:
    numSet = set(nums)
    longest = 0

    for num in numSet:
        if (num-1) not in numSet: # check if its a beginning of a sequence
            length = 1
            while (num+length) in numSet:
                length += 1
            longest = max(length, longest) #compares two value & returns larger one and assign it to longest
    return longest

#Time Complexity: O(n)
#Space Complexity : O(n)