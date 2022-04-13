# python_encoder_decoder
encoding and decoding algorithm in python

## Usage

```
usage: main.py [-h] [-i S [S ...]] [-e] [-d] [--bin] [--hex] [--rot13]

string encoder and decoder

options:
  -h, --help            show this help message and exit
  -i S [S ...], --input S [S ...]
                        data to encode or decode
  -e, --encode          encode data
  -d, --decode          decode data
  --bin                 set mode to binary
  --hex                 set mode to hexadecimal
  --rot13               set mode to rot13
```

## Example
```
python main.py (-e/--encode) (--bin/--hex/--rot13) -i <string>
python main.py (-d/--decode) (--bin/--hex/--rot13) -i <encoded-string>
```

## Using standalone files
```
python bin_encode.py <string>
python bin_decode.py <binary-string>
python hex_encode.py <string>
python hex_decode.py <hex-string>
python rot13_encode.py <string>
python rot13_decode.py <rot13-string>
```

## Future plans
> Other types of encoding and decoding  
> Caesar cipher  
> base64  
> etc.
