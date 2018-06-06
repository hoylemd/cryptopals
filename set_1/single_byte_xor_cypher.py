
def single_char_cypher_decode(cyphertext, key):
    xord_array = [0] * len(cyphertext)
    for i in range(len(cyphertext)):
        xord_array[i] = cyphertext[i] ^ key

    return bytes(xord_array)


def score_text(plaintext):
    f_map = {}
    for c in plaintext:
        if c in f_map.keys():
            f_map[c] += 1
        else:
            f_map[c] = 1

    return 0


def xor_cypher_cracker(cyphertext):
    from binascii import unhexlify

    key = 0

    cypher_bytes = unhexlify(cyphertext)
    out = single_char_cypher_decode(cypher_bytes, key)

    return key, out


def main():
    cyphertext = b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

    key, plaintext = xor_cypher_cracker(cyphertext)

    print(f"Best key was '{key}', which decrypted to '{plaintext}'")


if __name__ == '__main__':
    main()
