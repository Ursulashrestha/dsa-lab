nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# numsI = [0,1,1]
# Output: []

def threeSum(nums:list[int])-> list[list[int]]:
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if a>0:
            break

        if i > 0 and a == [nums - 1]:
            continue
        l = i + 1
        r = len(nums)-1
        while l < r:
            threeSum = a + nums[l]+ nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l]== nums[l-1]:
                    l += 1
    return res

#Time complexity: O(n^2)
#Space complexity: O(1) or O(n) extra space depending on the sorting algorithm.
#O(m) space for the output list.
# Where m is the number of triplets and n is the length of the given array.