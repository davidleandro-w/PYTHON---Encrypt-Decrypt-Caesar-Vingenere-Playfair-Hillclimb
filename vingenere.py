import main as mn


def vingenere(type, text, key):
    if mn.typeCheck(type) == 0:
        return "[The type you entered is wrong (" + type + ") only accept encrypt or decrypt]"
    textArray = mn.toArray(text)
    textValue = mn.toValue(textArray)
    keyArray = mn.toArray(key)
    keyValue = mn.toValue(keyArray)
    resultValue = []
    j = 0
    for i, v in enumerate(textValue):
        if j >= len(keyValue):
            j = 0
        if isinstance(v, int):
            if type == "encrypt":
                resultValue.insert(i, (textValue[i] + keyValue[j]) % 26)
            elif type == "decrypt":
                resultValue.insert(i, (textValue[i] - keyValue[j]) % 26)
            j += 1
        else:
            resultValue.insert(i, v)
    return ''.join(mn.toAlphabet(text, resultValue))


def run(text, keyVingenere):
    print("METODE VINGENERE")
    print("Plaintext  : " + text)
    vingenereEncrypt = vingenere("encrypt", text, keyVingenere)
    print("Encryption : " + vingenereEncrypt)
    vingenereDecrypt = vingenere("decrypt", vingenereEncrypt, keyVingenere)
    print("Decryption : " + vingenereDecrypt)
    print("")


if __name__ == '__main__':
    text = "Menjadikan Program Studi yang kompetitif, unggul, dan berteknologi (Komputek) pada tahun dua ribu dua puluh lima"
    # text = "David Leandro"
    keyVingenere = "sampaijumpalagi"
    run(text, keyVingenere)
