import random

FILE = 'norm_wiki_sample.txt'
GEN_LEN = 200
text = ''
INITIAL_TEXT = 'probability of'

def readFile(name):
    global text
    text = open(name, 'r').read()

def exercise1():
    frequencies = dict()
    counter = 0
    for word in text.split():
        if word not in frequencies.keys():
            frequencies[word] = 0
        frequencies[word] += 1
        counter += 1

    frequencies = {k: v / counter for k, v in frequencies.items()}
    frequencies = {k: v for k, v in sorted(frequencies.items(), key=lambda item: item[1], reverse=True)}
    return frequencies



def getWordByProbability(frequencies):
    randomValue = random.uniform(0, 1)
    pointer = 0
    for key, value in frequencies.items():
        pointer += value
        if randomValue <= pointer:
            return key

def exercise2(frequencies):
    text = ''
    for _ in range(GEN_LEN):
        text += str(getWordByProbability(frequencies)) + ' '
    return text
        


def getMarkovDictionary(text, level):
    markov = dict()
    tokens = text.split()
    key = tokens[:level]
    for word in tokens[level:]:
        merged = ' '.join(key)
        if merged not in markov.keys():
            markov[merged] = {}

        if word not in markov[merged].keys():
            markov[merged][word] = 1
        else:
            markov[merged][word] += 1

        key = key[1:] + [word]
    return markov

def getMarkovFrequencies(markov):
    for key in markov.keys():
        allKeyOccurences = sum(markov[key].values())
        for word in markov[key].keys():
            markov[key][word] /= allKeyOccurences
    return markov

def getWordByMarkovFrequencies(markovForSequence):
    randomValue = random.uniform(0, 1)
    pointer = 0
    for key, value in markovForSequence.items():
        pointer += value
        if randomValue <= pointer:
            return key

def exercise3(level):
    markov = getMarkovDictionary(text, level)
    markovFrequencies = getMarkovFrequencies(markov)
    resultText = ' '.join(INITIAL_TEXT.split()[:level])
    for _ in range(level, GEN_LEN):
        lastWords = ' '.join(resultText.split()[-level:])
        resultText += ' ' + getWordByMarkovFrequencies(markovFrequencies[lastWords])
    return resultText



def main():
    readFile(FILE)

    print('\nExercise 1:\n')
    frequencies = exercise1()
    wordsSum = sum(frequencies.values())
    print('Top 3 words:\n{}'.format(list(frequencies.items())[:3]))
    print('Last 3 words:\n{}'.format(list(frequencies.items())[-3:]))
    print('30k most popular words is {}% of all words'.format(round(30000 / wordsSum * 100, 2)))
    print('6k most popular words is {}% of all words\n'.format(round(6000 / wordsSum * 100, 2)))

    print('\nExercise 2:\n')
    firstLevel = exercise2(frequencies)
    print('First lvel:\n{}\n'.format(firstLevel))

    print('\nExercise 3:\n')
    print('Markov first level:\n{}\n'.format(exercise3(1)))
    print('Markov second level:\n{}\n'.format(exercise3(2)))

if __name__ == '__main__':
    main()
