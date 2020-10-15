import main as mn


def caesar(type, text, key):
    if mn.typeCheck(type) == 0:
        return "[The type you entered is wrong (" + type + ") only accept encrypt or decrypt]"
    textArray = mn.toArray(text)
    textValue = mn.toValue(textArray)
    mod = key % 26
    resultValue = []
    for index, x in enumerate(textValue):
        if isinstance(x, int):
            if type == "encrypt":
                cv = x + mod
            elif type == "decrypt":
                cv = x - mod
            if cv <= 25 and cv >= 0:
                resultValue.insert(index, cv)
            else:
                if type == "encrypt":
                    resultValue.insert(index, cv - 26)
                elif type == "decrypt":
                    resultValue.insert(index, cv + 26)
        elif x == " " or x == "," or x == "(" or x == ")" or x == ".":
            resultValue.insert(index, x)
    return ''.join(mn.toAlphabet(text, resultValue))


def run(text, keyCaesar):
    print("METODE CAESAR")
    print("Plaintext  : " + text)
    caesarEncrypt = caesar("encrypt", text, keyCaesar)
    print("Encryption : " + caesarEncrypt)
    caesarDecrypt = caesar("decrypt", caesarEncrypt, keyCaesar)
    print("Decryption : " + caesarDecrypt)
    print("")


if __name__ == '__main__':
    text = "Menjadikan Program Studi yang kompetitif, unggul, dan berteknologi (Komputek) pada tahun dua ribu dua puluh lima"
    # text = "David Leandro"
    keyCaesar = 125
    run(text, keyCaesar)
