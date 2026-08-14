file = open("day2/day2Input.txt", "r")
txt = file.readline()
lines = txt.split(",")
total = 0
firstID = 0
lastID = 0

for i in lines:
    line = i.split("-")
    firstID = int(line[0])
    lastID = int(line[1])
    num = firstID
    if not(len(str(firstID)) == len(str(lastID)) and len(str(firstID)) % 2 != 0):
        for j in range(firstID, lastID + 1):
            if len(str(num)) % 2 == 0:
                halfLen = int(len(str(num))/2)
                if str(num)[:halfLen] == str(num)[halfLen:]:
                    total += num
            num += 1

print(total)

