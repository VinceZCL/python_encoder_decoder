total = []
result = []
alphabets = ["A", "B", "C", "D", "E", "F"]

def convert(data):
    if data <= 9:
        return str(data)
    else:
        new_data = data - 10
        return alphabets[new_data]

def encode_hex(string):
    raw = " ".join(string)
    
    for i in raw:
        for j in i:
            k = ord(j)
            total.append(k)

    for i in total:
        first = i // 16
        last = i % 16
        final = convert(first) + convert(last)
        result.append(final)
    return result

if __name__ == "__main__":
    import sys

    if sys.argv[1:]:
        
        result = encode_hex(sys.argv[1:])
        print(*result)


    else:
        print("Please include arguments to encode to hexadecimal")