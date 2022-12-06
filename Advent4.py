
with open(r"C:\Users\wanke_daniel\Downloads\Advent4.txt", "r") as textFile:
    lines = textFile.read().splitlines()

# Question 1
count = 0
for line in lines:
    firstPairRange = line.split(",")[0]
    secondPairRange = line.split(",")[1]

    firstSectionNums = firstPairRange.split("-")
    secondSectionNums = secondPairRange.split("-")

    if int(secondSectionNums[0]) in list(range(int(firstSectionNums[0]), int(firstSectionNums[1])+1)) and int(secondSectionNums[1]) in list(range(int(firstSectionNums[0]), int(firstSectionNums[1])+1)):
        count += 1
    elif int(firstSectionNums[0]) in list(range(int(secondSectionNums[0]), int(secondSectionNums[1])+1)) and int(firstSectionNums[1]) in list(range(int(secondSectionNums[0]), int(secondSectionNums[1])+1)):
        count += 1

print(count)

# Question 2
count = 0
for line in lines:
    firstPairRange = line.split(",")[0]
    secondPairRange = line.split(",")[1]

    firstSectionNums = firstPairRange.split("-")
    secondSectionNums = secondPairRange.split("-")

    if int(secondSectionNums[0]) in list(range(int(firstSectionNums[0]), int(firstSectionNums[1])+1)) or int(secondSectionNums[1]) in list(range(int(firstSectionNums[0]), int(firstSectionNums[1])+1)):
        count += 1
    elif int(firstSectionNums[0]) in list(range(int(secondSectionNums[0]), int(secondSectionNums[1])+1)) or int(firstSectionNums[1]) in list(range(int(secondSectionNums[0]), int(secondSectionNums[1])+1)):
        count += 1

print(count)