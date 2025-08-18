# Encode and Decode String
strs = ["hello","world"]
output = "5#hello#world" # for encode
output2 = ["hello","world"] # for decode

def encode(strs:list[str])-> str:
    res=""
    for s in strs:
        res += str(len(s))+ "#"+ s
    return res

def decode(s:str)-> list[str]:
    res = []
    i = 0
    while i < len(s):
        j = i # j as new pointer to find #
        while s[j] != "#":
            j += 1 # move j until found #
        length = int(s[i:j])  # s[0:1] -> '5', s[0:2]-> '5#'
        i = j + 1
        j = i + length
        res.append(s[i:j])
        i = j
    return res

