import sys

total = []
result = []
alphabets = ["A", "B", "C", "D", "E", "F"]

def convert(data):
    if data <= 9:
        return str(data)
    else:
        new_data = data - 10
        return alphabets[new_data]

if sys.argv[1:]:
    
    raw = " ".join(sys.argv[1:])
    for i in raw:
        for j in i:
            k = ord(j)
            total.append(k)
    
    for i in total:
        first = i // 16
        last = i % 16
        final = convert(first) + convert(last)
        result.append(final)
    print(*result)


else:
    print("Please include arguments to encode to hexadecimal")