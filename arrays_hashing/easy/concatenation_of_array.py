# Concatenation of array
# nums - [2,2,1] , length of n
# Create an array called ans of length 2n

def concatArray(nums: list[int])-> list[int]:
    ans=[]
    for i in range(2): #Repeat the next steps 2 times
        for num in nums:
            ans.append(num)
        return ans #Add the number to the end of the list ans

# Time complexity: O(n)
# Space complexity: O(n)

def concatenateArray(nums: list[int]) -> list[int]:
    # Get the length of the list
    n = len(nums)
    # Creating a list to store the result which is twice the size of nums
    ans=[0] * (2*n) # [0,0,0,0,0,0]
    # ans[i] == nums[i]= ans[i+n]
    for index,num in enumerate(nums):
        ans[index] = num = ans[index+num]
        # loop one : i=0, num=2, n=3
        # ans[0] = ans[0+2]=> ans[2] = 2
        # ans[0]=2
        # ans[2] = 2
        #[2,0,0,2,0,0]-- after the first loop
    return ans

# Alternative
# def getConcatenate(nums: list[int]) -> list[int]:
#     return nums + nums
