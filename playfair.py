import main as mn


def text2D(type, text):
    textArrayFit = []
    textArray2 = []
    textArray1 = mn.toArray(text)
    a = 0
    for i, v in enumerate(textArray1):
        if v.isalpha():
            if type == "encrypt":
                if v == "j":
                    v = "i"
                if i > 0:
                    if textArrayFit[a - 1] != v:
                        textArrayFit.append(v)
                        a += 1
                    else:
                        if len(textArrayFit) % 2 != 0:
                            textArrayFit.append("z")
                            textArrayFit.append(v)
                            a += 2
                        else:
                            textArrayFit.append(v)
                            a += 1
                else:
                    textArrayFit.append(v)
                    a += 1
            elif type == "decrypt":
                textArrayFit.append(v)
    if type == "encrypt":
        if len(textArrayFit) % 2 > 0:
            textArrayFit.append("z")
    for i, v in enumerate(textArrayFit):
        if i % 2 == 0:
            textArray2.append([textArrayFit[i], textArrayFit[i + 1]])
    return textArray2


def key1D(type, key):
    keyArray = mn.toArray(key)
    keyArray1 = []
    a = 0
    for i, v in enumerate(keyArray):
        if v.isalpha():
            if v == "j":
                continue
            if i > 0:
                if v in keyArray1:
                    continue
                else:
                    keyArray1.append(v)
                    a += 1
            else:
                keyArray1.append(v)
                a += 1
    for i, v in enumerate(mn.alp):
        if v != "j":
            if v not in keyArray1:
                keyArray1.append(v)
    return keyArray1


def key2D(type, key):
    keyArray1 = key1D(type, key)
    keyArray2 = []
    a = 0
    for i in range(5):
        if type == "encrypt":
            keyArray2.append(
                [keyArray1[a], keyArray1[a + 1], keyArray1[a + 2], keyArray1[a + 3], keyArray1[a + 4],
                 keyArray1[a]])
            a += 5
            if a == 25:
                keyArray2.append([keyArray1[0], keyArray1[1], keyArray1[2], keyArray1[3], keyArray1[4],
                                  keyArray1[0]])
        elif type == "decrypt":
            if a == 0:
                keyArray2.append([keyArray1[24],
                                  keyArray1[20], keyArray1[21], keyArray1[22], keyArray1[23], keyArray1[24]])
            keyArray2.append([keyArray1[a + 4], keyArray1[a], keyArray1[a + 1], keyArray1[a + 2], keyArray1[a + 3],
                              keyArray1[a + 4]])
            a += 5
    return keyArray2


def result2D(type, textArray2, keyArray2):
    resultArray2 = []
    for i, v in enumerate(textArray2):
        A = 0
        B = 0
        for r in range(5):
            if A == 1 and B == 1:
                break
            for c in range(5):
                if type == "encrypt":
                    if v[0] == keyArray2[r][c]:
                        Ar = r
                        Ac = c
                        A = 1
                    if v[1] == keyArray2[r][c]:
                        Br = r
                        Bc = c
                        B = 1
                    if A == 1 and B == 1:
                        if Ar == Br:
                            resultArray2.append([keyArray2[Ar][Ac + 1], keyArray2[Br][Bc + 1]])
                            break
                        elif Ac == Bc:
                            resultArray2.append([keyArray2[Ar + 1][Ac], keyArray2[Br + 1][Bc]])
                            break
                        else:
                            resultArray2.append([keyArray2[Ar][Bc], keyArray2[Br][Ac]])
                            break
                elif type == "decrypt":
                    if v[0] == keyArray2[5 - r][5 - c]:
                        Ar = 5 - r
                        Ac = 5 - c
                        A = 1
                    if v[1] == keyArray2[5 - r][5 - c]:
                        Br = 5 - r
                        Bc = 5 - c
                        B = 1
                    if A == 1 and B == 1:
                        if Ar == Br:
                            resultArray2.append([keyArray2[Ar][Ac - 1], keyArray2[Br][Bc - 1]])
                            break
                        elif Ac == Bc:
                            resultArray2.append([keyArray2[Ar - 1][Ac], keyArray2[Br - 1][Bc]])
                            break
                        else:
                            resultArray2.append([keyArray2[Ar][Bc], keyArray2[Br][Ac]])
                            break
    return resultArray2


def result1D(type, resultArray2):
    result = []
    for i in range(len(resultArray2)):
        if type == "encrypt":
            result.append(resultArray2[i][0])
            result.append(resultArray2[i][1])
        if type == "decrypt":
            result.append(resultArray2[i][0])
            if i + 1 < len(resultArray2):
                if resultArray2[i][0] != resultArray2[i + 1][0] or resultArray2[i][1] != "z":
                    result.append(resultArray2[i][1])
                else:
                    continue
            else:
                result.append(resultArray2[i][1])
    return ''.join(result).upper()


def playfair(type, text, key):
    if mn.typeCheck(type) == 0:
        return "[The type you entered is wrong (" + type + ") only accept encrypt or decrypt]"
    textArray2D = text2D(type, text)
    keyArray2D = key2D(type, key)
    resultArray2D = result2D(type, textArray2D, keyArray2D)
    return result1D(type, resultArray2D)


def run(text, keyPlayfair):
    print("METODE PLAYFAIR")
    print("Plaintext  : " + text)
    playfairEncrypt = playfair("encrypt", text, keyPlayfair)
    print("Encryption : " + playfairEncrypt)
    playfairDecrypt = playfair("decrypt", playfairEncrypt, keyPlayfair)
    print("Decryption : " + playfairDecrypt)
    print("")


if __name__ == '__main__':
    text = "Menjadikan Program Studi yang kompetitif, unggul, dan berteknologi (Komputek) pada tahun dua ribu dua puluh lima"
    # text = "David Leandro"
    keyPlayfair = "sampaijumpalagi"
    run(text, keyPlayfair)
