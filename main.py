import caesar
import vingenere
import playfair
import hillclimb

alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
       "w",
       "x", "y", "z"]


def typeCheck(type):
    if type != "encrypt" and type != "decrypt":
        return 0
    else:
        return 1


def toArray(text):
    text = text.lower()
    textArray = []
    textArray[:0] = text
    return textArray


def toValue(textArray):
    textValue = []
    for i, x in enumerate(textArray):
        for index, y in enumerate(alp):
            if x == y:
                textValue.insert(i, index)
                break
            elif x == " " or x == "," or x == "(" or x == ")" or x == ".":
                textValue.insert(i, x)
                break
    return textValue


def toArray2(text):
    textArray = []
    text = text.lower()
    textArray[:0] = text
    result = []
    for i, x in enumerate(textArray):
        for index, y in enumerate(alp):
            if x == y:
                result.append(x)
                break
    return result


def toAlphabet(text, cipherValue):
    cipherText = []
    for i, x in enumerate(cipherValue):
        for index, y in enumerate(alp):
            if x == index:
                cipherText.insert(i, y)
                break
            elif x == " " or x == "," or x == "(" or x == ")" or x == ".":
                cipherText.insert(i, x)
                break
    for i, x in enumerate(text):
        if x.isupper():
            cipherText[i] = cipherText[i].upper()
    return cipherText


if __name__ == '__main__':
    text = "Menjadikan Program Studi yang kompetitif, unggul, dan berteknologi (Komputek) pada tahun dua ribu dua puluh lima"
    # text = "David Leandro"
    keyCaesar = 125
    keyVingenere = "sampaijumpalagi"
    keyPlayfair = "sampaijumpalagi"
    keyHillclimb = [[4, 6, 1],
                    [1, 4, 1],
                    [8, 5, 1]]

    caesar.run(text, keyCaesar)
    vingenere.run(text, keyVingenere)
    playfair.run(text, keyPlayfair)
    hillclimb.run(text, keyHillclimb)
    input()
