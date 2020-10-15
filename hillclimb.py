import main as mn
import numpy as np


def divide(textArray, lenKey):
    textDivide = []
    tempArray = []
    a = 0
    for i, v in enumerate(textArray):
        if v == " " or v == "," or v == "(" or v == ")" or v == ".":
            continue
        else:
            tempArray.append(v)
            a += 1
        if a == lenKey:
            textDivide.append(tempArray)
            tempArray = []
            a = 0
    return textDivide


def hillclimb(type, text, key):
    if mn.typeCheck(type) == 0:
        return "[The type you entered is wrong (" + type + ") only accept encrypt or decrypt]"
    if type == "encrypt":
        result = hillclimbEncrypt(text, key)
    elif type == "decrypt":
        result = hillclimbDecrypt(text, key)
    return result


def keyForDecrypt(key):
    a = np.array(key)
    det_a = int(np.linalg.det(a))
    if det_a % 2 == 0:
        return "Determinan genap, tidak dapat diproses"
    mod_a = det_a % 26
    x = 0
    for i in range(26):
        if (((i + 1) * mod_a) % 26) == 1:
            x = i + 1
    if x == 0:
        return "nilai 1 tidak dapat ditemukan"
    keyArray_divide = []
    if len(key) == 3:
        keyArray_divide.append([[key[1][1], key[1][2]], [key[2][1], key[2][2]]])
        keyArray_divide.append([[key[0][1], key[0][2]], [key[2][1], key[2][2]]])
        keyArray_divide.append([[key[0][1], key[0][2]], [key[1][1], key[1][2]]])

        keyArray_divide.append([[key[1][0], key[1][2]], [key[2][0], key[2][2]]])
        keyArray_divide.append([[key[0][0], key[0][2]], [key[2][0], key[2][2]]])
        keyArray_divide.append([[key[0][0], key[0][2]], [key[1][0], key[2][2]]])

        keyArray_divide.append([[key[1][0], key[1][1]], [key[2][0], key[2][1]]])
        keyArray_divide.append([[key[0][0], key[0][1]], [key[2][0], key[2][1]]])
        keyArray_divide.append([[key[0][0], key[0][1]], [key[1][0], key[1][1]]])

    elif len(key) == 2:
        return "2"
    keyArray_fit = [[], [], []]
    b = 1
    k = 0
    for i in range(len(key)):
        for j in range(len(key[0])):
            a = np.array(keyArray_divide[k])
            k += 1
            inv = int(round(np.linalg.det(a)))
            keyArray_fit[i].insert(j, ((((((inv) * b) % 26) * x)) % 26))  # (((((inv)*b)%26)*x))%26
            if b == 1:
                b = -1
            elif b == -1:
                b = 1
    return keyArray_fit


def resultValue(text, key):
    result = []
    for i, v in enumerate(text):
        for k in range(len(key)):
            Z = 0
            for j in range(1):
                for t in range(len(text[i])):
                    Z += key[k][t] * text[i][t]
                result.append(Z % 26)
    return result


def hillclimbEncrypt(text, key):
    textArray = mn.toArray2(text)
    mod = len(textArray) % len(key)
    if mod > 0:
        for i in range(mod + 1):
            textArray.append("z")
    textValue = mn.toValue(textArray)
    textDivide = divide(textValue, len(key))
    result = resultValue(textDivide, key)
    return ''.join(mn.toAlphabet(textArray, result)).upper()


def hillclimbDecrypt(text, key):
    textArray = mn.toArray(text)
    textValue = mn.toValue(textArray)
    textDivide = divide(textValue, len(key))
    keyInvers = keyForDecrypt(key)
    result = resultValue(textDivide, keyInvers)
    return ''.join(mn.toAlphabet(textArray, result)).upper()


def run(text, keyHillclimb):
    print("METODE HILLCLIMB")
    print("Plaintext  : " + text)
    hillclimbEncrypt = hillclimb("encrypt", text, keyHillclimb)
    print("Encryption : " + hillclimbEncrypt)
    hillclimbDecrypt = hillclimb("decrypt", hillclimbEncrypt, keyHillclimb)
    print("Decryption : " + str(hillclimbDecrypt))
    print("")


if __name__ == '__main__':
    text = "Menjadikan Program Studi yang kompetitif, unggul, dan berteknologi (Komputek) pada tahun dua ribu dua puluh lima"
    # text = "David Leandro"
    keyHillclimb = [[4, 6, 1],
                    [1, 4, 1],
                    [8, 5, 1]]
    run(text, keyHillclimb)
