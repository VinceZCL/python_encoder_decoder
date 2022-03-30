def encode_rot13(data):
    raw = "".join(data)
    out = str()
    for i in raw:
        asc = ord(i)
        if asc < 91:
            if asc < 78:
                asc += 13
            else:
                asc -= 13
            out += chr(asc)
        else:
            if asc < 110:
                asc += 13
            else:
                asc -=13
            out += chr(asc)
    return out

if __name__ == "__main__":
    import sys

    if sys.argv[1:]:
        
        result = encode_rot13(sys.argv[1:])
        print(result)


    else:
        print("Please include arguments to encode to rot13")