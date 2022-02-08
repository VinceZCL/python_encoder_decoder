# python_encoder_decoder
encoding and decoding algorithm in python

## Usage

```
usage: main.py [-h] [-i S [S ...]] [-e] [-d] [--bin] [--hex]

string encoder and decoder

options:
  -h, --help            show this help message and exit
  -i S [S ...], --input S [S ...]
                        data to encode or decode
  -e, --encode          encode data
  -d, --decode          decode data
  --bin                 set mode to binary
  --hex                 set mode to hexadecimal
```

## Using standalone files
```
python bin_encode.py <string>
python bin_decode.py <binarystring>
python hex_encode.py <string>
python hex_decode.py <hexstring>
```

## Future plans
> Other types of encoding and decoding  
> ROT13  
> Caesar cipher  
> base64  
> etc.
