
def single_char_cypher_decode(cyphertext, key):
    xord_array = [0] * len(cyphertext)
    for i in range(len(cyphertext)):
        xord_array[i] = cyphertext[i] ^ key

    return bytes(xord_array)


english_char_frequency = {
    'A': 8.167,
    'B': 1.492,
    'C': 2.782,
    'D': 4.253,
    'E': 12.702,
    'F': 2.228,
    'G': 2.015,
    'H': 6.094,
    'I': 6.966,
    'J': 0.153,
    'K': 0.772,
    'L': 4.025,
    'M': 2.406,
    'N': 6.749,
    'O': 7.507,
    'P': 1.929,
    'Q': 0.095,
    'R': 5.987,
    'S': 6.327,
    'T': 9.056,
    'U': 2.758,
    'V': 0.978,
    'W': 2.360,
    'X': 0.150,
    'Y': 1.974,
    'Z': 0.074,
}

english_chars = english_char_frequency.keys()


FAIL_SCORE = 99999


def score_text(plaintext):
    char_counts = {c: 0 for c in english_chars}
    skipped_chars = 0

    try:
        plaintext.decode('ascii')
    except UnicodeDecodeError:
        return FAIL_SCORE

    for c in plaintext:
        if c not in english_chars:
            skipped_chars += 1
            continue
        char_counts[c] = 1

    effective_length = len(plaintext) - skipped_chars

    def calc_frequency(n, l):
        try:
            return n / l
        except ZeroDivisionError:
            return 0

    f_chars = {c: calc_frequency(n, effective_length) for c, n in char_counts.items()}

    squared_errors = (
        (english_char_frequency[c] - f_chars[c]) ** 2  # chi-squared test as score
        for c in english_chars
    )
    score = sum(squared_errors)

    return score


def xor_cypher_cracker(cyphertext):
    from binascii import unhexlify

    top_chars = b' ETAO'

    char_counts = {}

    cypher_bytes = unhexlify(cyphertext)

    for c in cypher_bytes:
        if c in char_counts.keys():
            char_counts[c] += 1
        else:
            char_counts[c] = 1

    best_score = None
    best_key = None
    for c, _ in sorted(char_counts.items(), key=lambda i: i[1], reverse=True):
        for keystone in top_chars:
            key = keystone ^ c
            plaintext = single_char_cypher_decode(cypher_bytes, key)
            score = score_text(plaintext)
            if best_score is None or score < best_score:
                best_score = score
                best_key = key

    return best_key, single_char_cypher_decode(cypher_bytes, best_key)


def main():
    cyphertext = b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

    key, plaintext = xor_cypher_cracker(cyphertext)

    print(f"Best key was '{key}', which decrypted to '{plaintext}'")


if __name__ == '__main__':
    main()
