import numpy as np

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', ' ']
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']

content = ''
SIZE = 10000

def readFile(name):
    file = open(name, 'r')
    return file.read()


def getAverageLen(source = ''):
    totalLength = 0

    words = source.split()
    if (source == ''):
        words = content.split()

    for word in words:
        totalLength += len(word)

    return totalLength / len(words)


def generateSingleWord(lettersSource, probability):
    word = ''
    while True:
        char = np.random.choice(lettersSource, p=probability)
        if char == ' ':
            break
        else:
            word += char
    return word


def exercise1(printWords = False):
    total_length = 0
    probabilities = [1 / len(alphabet)] * len(alphabet)
    for _ in range(SIZE):
        word = generateSingleWord(alphabet, probabilities)
        if (printWords): print(word)
        total_length += len(generateSingleWord(alphabet, probabilities))

    return total_length / SIZE


def exercise2():
    lettersDictionary = {}
    counter = 0

    for letter in content:
        if letter not in lettersDictionary:
            lettersDictionary[letter] = 1
        else:
            lettersDictionary[letter] += 1
        counter += 1

    lettersDictionary = {k: v / counter for k, v in lettersDictionary.items()}

    return {k: v for k, v in sorted(lettersDictionary.items(), key=lambda item: item[1], reverse=True)}


def exercise3(frequency, printWords = False):
    keys = list(frequency.keys())
    probability_list = list(frequency.values())
    total_length = 0

    for _ in range(SIZE):
        word = generateSingleWord(keys, probability_list)
        total_length += len(word)
        if (printWords): print(word)

    return total_length / SIZE


def excercise4(letter):
    frequencies = {}
    for char in characters:
        frequencies[char] = 0

    counter = 0
    prevChar = content[0];
    for char in content[1:]:
        if (prevChar == letter):
            counter += 1
            frequencies[char] += 1
        
        prevChar = char
        
    if counter == 0:
        return frequencies

    return {k: v/counter for k, v in frequencies.items()}


def generateOccurencesDictionary(level):
    dictionary = {}

    for index, char in enumerate(content[level:]):
        key = content[index : level + index]

        if not key in dictionary:
                dictionary[key] = {}

        if char in dictionary[key]:
            dictionary[key][char] += 1
        else:
            dictionary[key][char] = 1

    return dictionary


def getProbabilities(dictionary):
    for key in dictionary:
        occurences = sum(dictionary[key].values())

        for childKey in dictionary[key]:
            if occurences != 0:
                dictionary[key][childKey] /= occurences

    return dictionary


def excercise5(textLen, level):
    occurencesDictionary = generateOccurencesDictionary(level)
    probabilitiesDictionary = getProbabilities(occurencesDictionary)
    
    text = content[:level]
    if level == 5:
        text = 'probability'

    for i in range(len(text), textLen):
        key = text[i - level : i]
        while key not in probabilitiesDictionary:
            index = np.randint(0, len(content))
            key = content[index : index + level]
        source = list(probabilitiesDictionary[key].keys())
        probabilities = list(probabilitiesDictionary[key].values())
        text += np.random.choice(source, p=probabilities)[0]
    
    return text


def main():
    global content
    files = ['norm_hamlet.txt', 'norm_romeo.txt', 'norm_wiki_sample.txt', 'bees.txt']
    content = readFile(files[2])
    print('\nFile = {}\tAverage length = {} characters'.format(files[2], getAverageLen()))


    # Excercise 1
    print('\nExercise 1:')
    print('\nWords = {}\tAverage length = {} characters'.format(SIZE, exercise1()))

    
    # Excercise 2
    frequencies = {}
    print('\nExercise 2:\n')
    frequencies = exercise2()
    for key, value in frequencies.items():
        print('\'{}\' = {}'.format(key, value))


    # Excercise 3
    print('\nExercise 3:')
    print('\nWords = {}\tAverage length = {} characters'.format(SIZE, exercise3(frequencies)))


    # Excercise 4
    print('\nExercise 4:\n')
    char = list(frequencies.keys())[0]
    dict = excercise4(char)

    print(char)
    for key in characters:
        print('\'{}\' after \'{}\' = {}'.format(key, char, dict[key]))
    
    char = list(frequencies.keys())[1]
    dict = excercise4(char)
    print('\n' + char)
    for key in characters:
        print('\'{}\' after \'{}\' = {}'.format(key, char, dict[key]))

    
    # Excercise 5
    print('\nExercise 5:')
    texts = []
    for index, level in enumerate(range(1, 6, 2)):
        texts.append(excercise5(SIZE, level))
        print('\nLevel {}:\n'.format(level))
        print(texts[index] + '\n')

    for text, level in zip(texts, range(1, 6, 2)):
        print('AVG word len of {} level = {}'.format(level, getAverageLen(text)))



if __name__ == '__main__':
    main()