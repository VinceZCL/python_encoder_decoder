import sys

final = []

def binary(data):
    
    b2 = ""
    asc = ord(data)

    if asc // 128:
        b2 += "1"
        asc -= 128
    else:
        b2 += "0"

    if asc // 64:
        b2 += "1"
        asc -= 64
    else:
        b2 += "0"

    if asc // 32:
        b2 += "1"
        asc -= 32
    else:
        b2 += "0"
    
    if asc // 16:
        b2 += "1"
        asc -= 16
    else:
        b2 += "0"

    if asc // 8:
        b2 += "1"
        asc -= 8
    else:
        b2 += "0"

    if asc // 4:
        b2 += "1"
        asc -= 4
    else:
        b2 += "0"
    
    if asc // 2:
        b2 += "1"
        asc -= 2
    else:
        b2 += "0"
    
    if asc:
        b2 += "1"
    else:
        b2 += "0"
    
    return b2

if sys.argv[1:]:
    
    raw = " ".join(sys.argv[1:])

    for i in raw:
        j = binary(i)
        final.append(j)
    
    print(*final)

else:
    print("Please include argument to encode to binary")