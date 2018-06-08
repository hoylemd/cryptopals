from single_byte_xor_cypher import xor_cypher_cracker, score_text


def main():
    with open('4_data.txt') as fp:
        lines = fp.read().split('\n')

    decrypts = {}
    for line in lines:
        _, plaintext = xor_cypher_cracker(line)
        decrypts[line] = plaintext

    best_score = None
    best_line = None
    for line, decrypt in decrypts.items():
        score = score_text(decrypt)
        if best_score is None or score < best_score:
            best_score = score
            best_line = line

    print(f"Best decrypt was: {decrypts[best_line]} from {best_line}")


if __name__ == '__main__':
    main()
