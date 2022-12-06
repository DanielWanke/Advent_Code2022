import re
with open(r"C:\Users\wanke_daniel\Downloads\Advent6.txt", "r") as textFile:
    lines = textFile.readline()

    # Question 1
    charCount = 0
    while charCount+4 <= len(lines)-1:
        inp = lines[charCount:charCount+4]
        match = re.search(r'^(?!.*(.).*\1)[A-Za-z0-9]+$', inp)
        if match:
            print("Question 1")
            print(match)
            print(charCount+4)
            break
        charCount += 1

    # Question 2
    charCount = 0
    while charCount+14 <= len(lines)-1:
        inp = lines[charCount:charCount+14]
        match = re.search(r'^(?!.*(.).*\1)[A-Za-z0-9]+$', inp)
        if match:
            print("Question 2")
            print(match)
            print(charCount+14)
            break
        charCount += 1