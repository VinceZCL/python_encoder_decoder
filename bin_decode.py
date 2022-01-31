import sys

fraw = []
result = []

"""
0 - 128 i0
1 - 64 i1
0 - 32 i2
0 - 16 i3
0 - 8 i4
0 - 4 i5
0 - 2 i6
1 - 1 i7
"""

def check(data):
    asc = 0
    if int(data[0]):
        asc += 128
    if int(data[1]):
        asc += 64
    if int(data[2]):
        asc += 32
    if int(data[3]):
        asc += 16
    if int(data[4]):
        asc += 8
    if int(data[5]):
        asc += 4
    if int(data[6]):
        asc += 2
    if int(data[7]):
        asc += 1
    return asc

if sys.argv[1:]:
    
    raw = "".join(sys.argv[1:])
    for i in range(0, len(raw), 8):
        fraw.append(raw[i:i+8])
    
    for i in fraw:
        asc = check(i)
        char = chr(asc)
        result.append(char)
    print(*result)

else:
    print("Please include arguments to decode from binary")