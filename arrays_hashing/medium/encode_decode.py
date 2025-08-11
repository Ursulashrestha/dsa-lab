# Encode and Decode String
strs = ["I","am", "tired"]
output = "1#I2#am5#tired" # for encode
output2 = ["I","am", "tired"] # for decode

def encode(strs:list[str])-> str:
    res=""
    for s in strs:
        res += str(len(s))+ "#"+ s
    return res

