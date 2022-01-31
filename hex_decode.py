import sys

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

if sys.argv[1:]:

    if len(sys.argv[1]) > 2:
        raw = "".join(sys.argv[1:])
        for i in range(0, len(raw), 2):
            new_raw.append(raw[i:i+2])
    else:
        new_raw = (list(sys.argv[1:]))

    for i in new_raw:
        first = check(i[0])
        last = check(i[-1])
        final = (first * 16) + last
        result += chr(final)
        
    new_result = "".join(result)
    print(new_result)


else:
    print("Please include arguments to decode from hexadecimal")