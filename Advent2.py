with open(r"C:\Users\wanke_daniel\Downloads\Advent2.txt", "r") as textFile:
     lines = textFile.read().splitlines()
scores = []
for line in lines:
 if line == "A Y":
     scores.append(8)
 elif line == "A X":
     scores.append(4)
 elif line == "A Z":
     scores.append(3)
 elif line == "B Y":
     scores.append(5)
 elif line == "B X":
     scores.append(1)
 elif line == "B Z":
     scores.append(9)
 elif line == "C Y":
     scores.append(2)
 elif line == "C X":
     scores.append(7)
 elif line == "C Z":
     scores.append(6)
print(sum(scores))

scores = []
for line in lines:
    if line == "A Y":
        scores.append(4)
    elif line == "A X":
        scores.append(3)
    elif line == "A Z":
        scores.append(8)
    elif line == "B Y":
        scores.append(5)
    elif line == "B X":
        scores.append(1)
    elif line == "B Z":
        scores.append(9)
    elif line == "C Y":
        scores.append(6)
    elif line == "C X":
        scores.append(2)
    elif line == "C Z":
        scores.append(7)
print(sum(scores))