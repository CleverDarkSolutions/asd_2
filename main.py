from pathlib import Path


def count(sequence):
    result = []
    sequence = sorted(sequence)
    sequence = list(sequence)
    for i in sequence:
        if i not in result:
            result.append(i)
    dictionary = []
    listOne = []
    listTwo = []
    for a in result:
        n = 0
        for letter in sequence:
            if letter == a:
                n += 1
        listOne.append(a)
        listTwo.append(n)
    dictionary.append(listOne)
    dictionary.append(listTwo)
    return dictionary


def heapify(i, list):
    l = 2 * i + 1
    r = 2 * i + 2
    if l < len(list[0]) and list[1][l] > list[1][i]:
        largest = l
    else:
        largest = i
    if r < len(list[0]) and list[1][r] > list[1][largest]:
        largest = r
    if largest != i:
        list[0][i], list[0][largest] = list[0][largest], list[0][i]
        list[1][i], list[1][largest] = list[1][largest], list[1][i]
        heapify(largest, list)


def buildHeap(list):
    i = len(list[0]) // 2
    while i >= 0:
        heapify(i, list)
        i -= 1


def findMin(list):
    key = list[0][0]
    value = list[1][0]
    i = 0
    index = 0
    for element in list[1]:
        if element <= value:
            key = list[0][i]
            value = element
            index = i
        i += 1
    del list[0][index]
    del list[1][index]
    buildHeap(list)
    return key, value


def insert(list, key, value):
    list[0].append(key)
    list[1].append(value)
    buildHeap(list)


def results(strInput):
    dictionary = count(strInput)
    listTwo = {}
    while len(dictionary[0]) != 1:
        key1, value1 = findMin(dictionary)
        key2, value2 = findMin(dictionary)
        if value1 < value2:
            name = key1 + key2
            listTwo[key1] = value1
            listTwo[key2] = value2
            listTwo[name] = value1 + value2
        else:
            name = key2 + key1
            listTwo[key2] = value2
            listTwo[key1] = value1
            listTwo[name] = value1 + value2
        insert(dictionary, name, value1 + value2)
    return produceDictionary(list(listTwo.keys()))


def encodeSign(letter, list):
    binary = ""
    for key in list:
        if key != letter:
            if key.startswith(letter):
                letter = key
                binary += "0"
            elif key.endswith(letter):
                letter = key
                binary += "1"
    return binary[::-1]


def produceDictionary(list):
    dictionary = {}
    for letter in list:
        if len(letter) == 1:
            dictionary[letter] = encodeSign(letter, list)
    return dictionary


def encryptAll(path):
    txt = Path(path).read_text(encoding="utf-8")
    lengthOfFile = len(txt)
    txt = txt + txt[-1] * (lengthOfFile % 8)
    dictionary = results(txt)
    txt = list(txt)
    for item in txt:
        txt[txt.index(item)] = dictionary[item]
    arr = ''
    for char in txt:
        arr += char
    i = 9
    while i < len(arr):
        arr = arr[0:i] + " " + arr[i:]
        i += 9
    arr = arr.split(" ")
    asciiString = ''
    file = open("encoded" + path, "w+", encoding="utf-8")
    print("Length: " + str(lengthOfFile))
    for item in arr:
        a = int(item, 2)
        asciiCharacter = chr(a)
        file.write(asciiCharacter)
        asciiString += asciiCharacter
    file.close()


encryptAll("inputOne.txt")
print(results("asdgdfreq"))
