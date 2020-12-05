import numpy as np

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', ' ']
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']

def readFile(name):
    file = open(name, 'r')
    return file.read()


def fileParameters(filename):
    content = readFile(filename)
    totalLength = 0
    words = content.split(' ')

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


def exercise1(size):
    total_length = 0
    probability = [1 / len(alphabet)] * len(alphabet)
    for _ in range(size):
        total_length += len(generateSingleWord(alphabet, probability))

    return total_length / size


def exercise2(filename):
    content = readFile(filename)
    letters = {}
    counter = 0

    for letter in content:
        cardinality = letters.get(letter, 0)
        letters.update({letter: cardinality + 1})
        counter += 1

    for letter in letters:
        letters.update({letter: letters.get(letter) / counter})

    return {k: v for k, v in sorted(letters.items(), key=lambda item: item[1], reverse=True)}


def exercise3(size, frequency):
    keys = list(frequency.keys())
    print(keys)
    probability_list = list(frequency.values())
    print(probability_list)
    total_length = 0

    for _ in range(size):
        total_length += len(generateSingleWord(keys, probability_list))

    return total_length / size


def excercise4(filename, letter):
    content = readFile(filename)
    
    frequencies = {}
    for char in characters:
        frequencies[char] = 0

    counter = 0
    saveNextChar = False
    for char in content:
        if (saveNextChar):
            counter += 1
            frequencies[char] += 1
            saveNextChar = False
            continue
        elif (char == letter):
            saveNextChar = True
    
    return frequencies, counter


def getProbability(sampleText, word):
    pass


def excercise5(sampleText, markovLen, filename):
    firstWord = 'probability';
    word = firstWord[len(firstWord) - markovLen:]
    textLen = 1000
    newWord = firstWord

    while(len(newWord) < textLen):
        probability = getProbability(sampleText, word)
        if sum(probability) == 0:
            newWord += " "
        # else:
            # newWord += generateWithProbability(readFile(filename), 1, probability)
        word = newWord[len(newWord) - markovLen:]
    return newWord



def main():
    files = ['norm_hamlet.txt', 'norm_romeo.txt', 'norm_wiki_sample.txt', 'bees.txt']
    # for filename in files:
    print('File =', files[2], '\tAverage length =', fileParameters(files[2]), 'characters')

    # Excercise 1
    size = 2000
    print('\nExercise 1:\nWords =', size, '\tAverage length =', exercise1(size), 'characters')

    
    # Excercise 2
    frequency = {}
    print('\nExercise 2:')
    # for filename in files:
    frequency = exercise2(files[2])
    print('\nFile =', files[2], '\nLetters:\n', frequency)


    # Excercise 3
    print('\nExercise 3:')
    print('\nWords = ', size, '\tAverage length =', exercise3(size, frequency), 'characters')


    # Excercise 4
    print('\nExercise 4:\n')
    char = list(frequency.keys())[0]
    dic, counter = excercise4(files[2], char)
    print(char)
    for key, value in dic.items():
        print('\'{}\' after \'{}\' = {}'.format(key, char, value/counter))
    
    char = list(frequency.keys())[1]
    dic, counter = excercise4(files[2], char)
    print('\n' + char)
    for key, value in dic.items():
        print('\'{}\' after \'{}\' = {}'.format(key, char, value/counter))

    
    # Excercise 5
    print('\nExercise 5:')

if __name__ == '__main__':
    main()