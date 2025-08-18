# Top K frequent elements
# nums = [1,1,1,2,2,3]
# k = 2
# output = [1,2]

# def topkFrequent(nums: list[int], k: int)-> list[int]:
#     count = {}

#     freq = [[] for i in range(len(nums)+ 1)]

#     for num in nums:
#         count[num]= 1+ count.get(num,0)

#     for num,cnt in count.items():
#         freq[cnt].append(num)

#     res=[]
#     for i in range(len(freq) -1,0,1):
#         for num in freq[i]:
#             res.append(num)
#             if len(res) == k:
#                 return res

#Encode and decode string
def encode(strs:list[str])-> str:
    res= ""
    for s in strs:
        res += str(len(s))+ "#"+ s
    return res

def decode(word:str) -> list[str]:
    result = []
    i = 0
    while i<len(word):
        j = i
        while word[j]!= "#":
            j +=1
        length = word[i:j]
        i = j+1
        j = i+length
        result.append(word[i:j])
        i=j
    return result












































            