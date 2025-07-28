# if an array contains duplicate, return true
# if an array is distinct or has no duplicate, return false

def containsDuplicate(nums):
    seen = set()  # empty set to store distinct elements

    for num in nums: # loop through each num in the list
        if num in seen: # condition to check if num is already stored in the set.
            return True # returns true if the condition meets
        seen.add(num) # otherwise add it in the set
    return False # after checking all the elements and no repeats found

# Time complexity : O(n)
# Space complexity : O(n)