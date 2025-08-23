height = [1,8,6,2,5,4,8,3,7]
#output = int -- an area

def maxArea(height:list[int])-> int:
    l = 0
    r = len(height)-1
    res = 0
    while l<r:
        w = r-l
        h = min(height[l], height[r])
        area = w*h
        res = max(area, res)
        if height[l]<= height[r]:
            l+=1
        else:
            r-=1
    return res
#Time complexity : O(n)
#Space COmplexity: O(1)