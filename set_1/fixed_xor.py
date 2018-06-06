

def fixed_or(first, second):
    xord_array = [0] * len(first)
    for i in range(len(first)):
        xord_array[i] = first[i] ^ second[i]

    return bytes(xord_array)


def fixed_or_wrapper(first, second):
    from binascii import unhexlify, hexlify
    if len(first) != len(second):
        raise ValueError('input strings are of different lengths')

    first = unhexlify(first)
    second = unhexlify(second)

    out = fixed_or(first, second)

    return hexlify(out)


def main():
    first = b'1c0111001f010100061a024b53535009181c'
    second = b'686974207468652062756c6c277320657965'

    expected = b'746865206b696420646f6e277420706c6179'
    actual = fixed_or_wrapper(first, second)

    if expected != actual:
        print('Nope')
        print(f"expected: {expected}")
        print(f"actual  : {actual}")
    else:
        print('OK!')


if __name__ == '__main__':
    main()
