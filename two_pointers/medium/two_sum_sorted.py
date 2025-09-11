# Two Sum II - Input Array Is Sorted 
numbers= [2,7,11,15]
target=9
#Output = [1,2]
#The solution must use only constant extra space

def twoSum(numbers:list[int], target:int)->list[int]:
    l = 0
    r = len(numbers)-1
    while l<r:
        curSum = numbers[l]+numbers[r]
        if curSum>target:
            r-=1
        elif curSum<target:
            l+=1
        else:
            return[l+1, r+1]
    return [] #a function that finishes without return would give back None, its safety net
#Time complexity: O(n)
#Space complexity: O(1)