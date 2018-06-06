

def hex_to_b64(hex_bytes):
    from binascii import unhexlify
    bstring = unhexlify(hex_bytes)

    from base64 import b64encode
    return b64encode(bstring)


def main():
    hex = (
        "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d7573687"
        "26f6f6d"
    )

    expected_b64 = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    got = hex_to_b64(hex)
    if got != expected_b64:
        print("Nope")
        print(f"expected: {expected_b64}")
        print(f"actual  : {got}")
    else:
        print('OK!')


if __name__ == '__main__':
    main()
