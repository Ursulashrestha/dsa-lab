#Trapping Rain Water
def trap(height:list[int])-> int:
    if not height: # if no blocks, no water
        return 0
    l = 0
    r = len(height)-1
    leftMax = height[l] #tallest block from left
    rightMax = height[r] #tallest block from right
    res = 0
    while l<r:
        # if the tallest left wall is shoter than tallest right 
        if leftMax<rightMax:
            l+=1
            leftMax = max(leftMax, height[l])
            res+= leftMax - height[l]
        else:
            r-=1
            rightMax = max(rightMax,height[r])
            res+= rightMax - height[r]
    return res




