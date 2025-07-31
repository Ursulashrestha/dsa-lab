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


# Alternative
# def getConcatenate(nums: list[int]) -> list[int]:
#     return nums + nums
