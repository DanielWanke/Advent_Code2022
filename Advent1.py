elves = {}
with open(r"C:\Users\wanke_daniel\Downloads\Advent1.txt", "r") as textFile:
    lines = textFile.read().splitlines()

    elvCount = 0
    for line in lines:
        if line == '':
            elvCount += 1
            elves[elvCount] = []
        else:
            elves[elvCount].append(int(line))

totalCaloriesPerElv = {}
for elv, snacks in elves.items():
    print(elv, sum(snacks))
    totalCaloriesPerElv[elv] = sum(snacks)

highestCalorie = 0
for k,v in totalCaloriesPerElv.items():
    if v > highestCalorie:
        highestCalorie = v
        print("Elv: "+str(k), "Tot Calorie: "+str(v))

print(sum(sorted(totalCaloriesPerElv.values(), reverse=True)[:3]))