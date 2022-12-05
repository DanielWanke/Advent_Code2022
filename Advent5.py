import re
with open(r"C:\Users\wanke_daniel\Downloads\Advent5.txt", "r") as textFile:
    lines = textFile.read().splitlines()

columns = {}
count=1
while count<10:
    columns[count]=[]
    count+=1

for line in lines[:8]:
    if line[1] != " ":
        columns[1].append(line[1])
    if line[5] != " ":
        columns[2].append(line[5])
    if line[9] != " ":
        columns[3].append(line[9])
    if line[13] != " ":
        columns[4].append(line[13])
    if line[17] != " ":
        columns[5].append(line[17])
    if line[21] != " ":
        columns[6].append(line[21])
    if line[25] != " ":
        columns[7].append(line[25])
    if line[29] != " ":
        columns[8].append(line[29])
    if line[33] != " ":
        columns[9].append(line[33])

tableDict = {}
for k, v in columns.items():
    tableDict[k] = []
    for values in reversed(v):
        tableDict[k].append(values)

for line in lines[10:]:
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
