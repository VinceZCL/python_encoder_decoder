def decode_rot13(data):
    raw = " ".join(data)
    out = str()
    for i in raw:
        if i == " ":
            out += i
        else:
            asc = ord(i)
            if asc < 91:
                if asc < 78:
                    asc += 13
                else:
                    asc -=13
            else:
                if asc < 110:
                    asc += 13
                else:
                    asc -= 13
            out += chr(asc)
    return out

if __name__ == "__main__":
    import sys

    if sys.argv[1:]:

        result = decode_rot13(sys.argv[1:])
        print(result)
    
    else:
        print("Please include arguments to decode from rot13")