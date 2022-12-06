
with open(r"C:\Users\wanke_daniel\Downloads\Advent3.txt", "r") as textFile:
    lines = textFile.read().splitlines()

# Question 1
scores = []
for line in lines:
    firstHalf = line[:int(len(line)/2)]
    secondHalf = line[int(len(line)/2):]

    for char in firstHalf:
        if char in secondHalf:
            if char.isupper():
                score = ord(char) - 38
            else:
                score = ord(char) - 96
            scores.append(score)
            break

print(sum(scores))

# Question 2
scores = []

count = 0
while count < len(lines):
    for char in lines[count]:
        if char in lines[count+1] and char in lines[count+2]:
            if char.isupper():
                score = ord(char) - 38
            else:
                score = ord(char) - 96
            scores.append(score)
            break
    count += 3

print(sum(scores))