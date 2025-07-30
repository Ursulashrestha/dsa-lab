# Given
# nums = [2,7,11,15]
# target = 9
# Todo: Return indices of the two numbers in nums that they add up to target
# Output: [0,1]

def twoSum(nums:list[int], target:int) -> list[int]:
    seen = {} # create an empty dict to store num
    # seen= {2: 0}

    for index, num in enumerate(nums):
        needed = target - num
             #1st loop
               # = 9 - 2
               # = 7
        # so is needed which is 7 in seen, NO because its empty 
        # seen now will look like {2: 0}
        # seen[2] = 0
        
        if needed in seen: # checking if needed 7 is in seen
            return [seen[needed], index] # the index of num seen before and current
        seen[num]=index

# Time Complexity: O(n)
# Space Complexity: O(n)

