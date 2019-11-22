#!python
# Takes input from a text file, displays a count of words from the file in descending order
import re
import collections
import operator

while True:
    try:
        textFile = input('Enter name of txt file: ')
        textFile = textFile + '.txt'
        file = open(textFile, 'r', encoding='utf8')
        break
    except:
        print('File not found!')
        continue
        
while True:
    try:
        wordMinimum = int(input('Show me words that occur more than ___ times: '))
        break
    except:
        print('Please enter a number.')
        continue

wordsToFilter = ['THE', 'BE', 'AND', 'OF', 'A', 'IN', 'TO', 'HAVE', 'IT', 'I', 'THAT', 'FOR', 'YOU', 'HE', 'WITH', 'ON',
                'DO', 'SAY', 'THIS', 'THEY', 'IS', 'AN', 'AT', 'BUT', 'WE', 'HIS', 'FROM', 'THAT', 'NOT', 'BY', 'SHE',
                'OR', 'AS', 'WHAT', 'GO', 'THEIR', 'CAN', 'WHO', 'GET', 'IF', 'WOULD', 'HER', 'ALL', 'MY', 'MAKE', 'ABOUT',
                'KNOW', 'WILL', 'AS', 'UP', 'ONE', 'TIME', 'HAS', 'BEEN', 'THERE', 'YEAR', 'SO', 'THINK', 'WHEN', 'WHICH',
                'THEM', 'SOME', 'ME', 'PEOPLE', 'TAKE', 'OUT', 'INTO', 'JUST', 'SEE', 'HIM', 'YOUR', 'COME', 'COULD', 'NOW',
                'THAN', 'LIKE', 'OTHER', 'HOW', 'THEN', 'ITS', 'OUR', 'TWO', 'MORE', 'THESE', 'WANT',
                'WAY', 'LOOK', 'FIRST', 'ALSO', 'NEW', 'BECAUSE', 'DAY', 'MORE', 'USE',
                'NO', 'MAN', 'FIND', 'HERE', 'THING', 'GIVE', 'MANY', 'WELL', 'WAS', 'HAD', 'SAID']

wordList = []
wordListTotal = []
wordDictionary = {}

for line in file:
    words = line.split()
    for word in words:
        word = word.upper()
        word = re.sub(r'[^\w\s]','', word)
        if word not in wordsToFilter:
            wordList.append(word)
            if word not in wordListTotal:
                wordListTotal.append(word)

for word in wordListTotal:
    if wordList.count(word) > wordMinimum:
        wordDictionary[word] = wordList.count(word)
    else: continue

sortedDict = sorted(wordDictionary.items(), key = operator.itemgetter(1), reverse = True)

for pair in sortedDict:
    print(pair[0] + ": " + str(pair[1]))


input('PRESS ENTER TO EXIT')
