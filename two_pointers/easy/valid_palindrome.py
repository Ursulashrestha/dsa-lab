#Valid Palindrome
s = "Was it a car or a cat I saw?"
# Output: true

# Method I
def isPalindrome(s:str)-> bool:
    newStr = ""
    for char in s:
        if char.isalnum(): #skips space, comma, colon etc
            newStr += char.lower()
    return newStr == newStr[::-1]

#Time Complexity = O(n)
#Space Complexity = O(n)