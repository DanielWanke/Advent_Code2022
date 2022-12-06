
with open(r"C:\Users\wanke_daniel\Downloads\Advent3.txt", "r") as textFile:
    lines = textFile.read().splitlines()

# Question 1
sameLetters = []
for line in lines:
    firstHalf = line[:int(len(line)/2)]
    secondHalf = line[int(len(line)/2):]

    for char in firstHalf:
        if char in secondHalf:
            sameLetters.append(char)
            break

scores = []
for letter in sameLetters:
    if letter.isupper():
        score = ord(letter)-38
    else:
        score = ord(letter)-96
    scores.append(score)

print(sum(scores))

# Question 2
sameLetters = []

count = 0
while count < len(lines):
    for char in lines[count]:
        if char in lines[count+1] and char in lines[count+2]:
            sameLetters.append(char)
            break
    count += 3

scores = []
for letter in sameLetters:
    if letter.isupper():
        score = ord(letter)-38
    else:
        score = ord(letter)-96
    scores.append(score)

print(sum(scores))
