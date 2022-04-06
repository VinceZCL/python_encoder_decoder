# import bin_decode
# import bin_encode
# import hex_decode
# import hex_encode
import argparse

desc = "string encoder and decoder"
parser = argparse.ArgumentParser(description=desc)

parser.add_argument("-i", "--input", type=str, nargs="+", metavar="S", help="data to encode or decode")
parser.add_argument("-e", "--encode", help="encode data", action='store_true')
parser.add_argument("-d", "--decode", help="decode data", action='store_true')
# parser.add_argument("-m", "--mode", metavar="M", help="set mode (h->hexadecimal) (b->binary)")
parser.add_argument("--bin", help="set mode to binary", action="store_true")
parser.add_argument("--hex", help="set mode to hexadecimal", action="store_true")
parser.add_argument("--rot13", help="set mode to rot13", action="store_true")

args = parser.parse_args()

if args.bin:
    if args.encode:
        import bin_encode

        result = bin_encode.encode_binary(args.input)
        print(*result)

    elif args.decode:
        import bin_decode

        result = bin_decode.decode_binary(args.input)
        print(result)

elif args.hex:
    if args.encode:
        import hex_encode

        result = hex_encode.encode_hex(args.input)
        print(*result)

    elif args.decode:
        import hex_decode

        result = hex_decode.decode_hex(args.input)
        print(result)

elif args.rot13:
    if args.encode:
        import rot13_encode
        result = rot13_encode.encode_rot13(args.input)
        print(result)
    elif args.decode:
        import rot13_decode
        result = rot13_decode.decode_rot13(args.input)
        print(result)