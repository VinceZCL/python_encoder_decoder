result = ""
new_raw = []

def check(data):
    
    try:
        new = int(data)
        return new

    except:
        new = ord(data)
        new_new = new -  55
        return new_new

def decode_hex(string):
    global result
    raw = "".join(string)
    for i in range(0, len(raw), 2):
        new_raw.append(raw[i:i+2])
    
    for i in new_raw:
        first = check(i[0])
        last = check(i[-1])
        final = (first * 16) + last
        result += chr(final)
    return result

if __name__ == "__main__":
    import sys

    if sys.argv[1:]:

        result = decode_hex(sys.argv[1:])
        print(result)

    else:
        print("Please include arguments to decode from hexadecimal")