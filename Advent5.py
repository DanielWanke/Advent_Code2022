tableDict = {1: ['H','B','V','W','N','M','L','P'],
             2: ['M','Q','H'],
             3: ['N','D','B','G','F','Q','M','L'],
             4: ['Z','T','F','Q','M','W','G'],
             5: ['M','T','H','P'],
             6: ['C','B','M','J','D','H','G','T'],
             7: ['M','N','B','F','V','R'],
             8: ['P','L','H','M','R','G','S'],
             9: ['P','D','B','C','N']}

import re
with open(r"C:\Users\wanke_daniel\Downloads\Advent5.txt", "r") as textFile:
    lines = textFile.read().splitlines()

    for line in lines:
        tempDict = {}

        numbersInLine = re.findall('\d+', line)
        amountToMove = int(numbersInLine[0])
        fromColumn = int(numbersInLine[1])
        toColumn = int(numbersInLine[2])

        startingIndex = len(tableDict.get(fromColumn))-amountToMove
        valuesToMove = tableDict.get(fromColumn)[startingIndex:]

        for k,v in tableDict.items():
            if k != fromColumn and k != toColumn:
                tempDict[k] = v
            elif k == fromColumn:
                tempDict[k] = tableDict.get(fromColumn)[:startingIndex]
            elif k == toColumn:
                tempDict[k] = tableDict.get(toColumn)
                for value in valuesToMove:
                    tempDict[k].append(value)

        tableDict = tempDict

for k, v in tempDict.items():
    print(k, v)