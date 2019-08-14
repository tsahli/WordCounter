#!python
# Takes input from a text file, displays a count of words from the file in descending order
import re
import collections
import operator

while True:
    try:
        textFile = raw_input('Enter name of txt file: ')
        textFile = textFile + '.txt'
        file = open(textFile, 'r')
        break
    except:
        print('File not found!')
        continue
        
while True:
    try:
        wordMinimum = int(raw_input('Show me words that occur more than ___ times: '))
        break
    except:
        print('Please enter a number.')
        continue
        
wordList = []
wordListTotal = []
wordDictionary = {}

for line in file:
    words = line.split()
    for word in words:
        word = word.upper()
        word = re.sub(r'[^\w\s]','', word)
        wordList.append(word)
        if word not in wordListTotal:
            wordListTotal.append(word)

for word in wordListTotal:
    if wordList.count(word) > wordMinimum:
        wordDictionary[word] = wordList.count(word)
    else: continue

sortedDict = sorted(wordDictionary.items(), key = operator.itemgetter(1), reverse= True)

for pair in sortedDict:
    print(pair[0] + ": " + str(pair[1]))


input('PRESS ENTER TO EXIT')
