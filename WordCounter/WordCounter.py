#!python
import re

textFile = raw_input('Enter name of txt file: ')
textFile = textFile + '.txt'
file = open(textFile, 'r')

wordList = []
wordListTotal = []

for line in file:
    words = line.split()
    for word in words:
        word = word.upper()
        word = re.sub(r'[^\w\s]','', word)
        wordList.append(word)
        if word not in wordListTotal:
            wordListTotal.append(word)

for word in wordListTotal:
    if wordList.count(word) > 50:
        print(word + ": " + str(wordList.count(word)))
    else: continue

input('PRESS ENTER TO EXIT')
