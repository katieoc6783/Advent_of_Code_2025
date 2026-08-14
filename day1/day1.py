file = open("day1Input.txt", "r")
line = file.readline()
num = 50
passw = 0
while line:
    line = line.strip()
    lineNum = int(line[1:])
    if line[:1] == "R":
    #we increase
        num = num + lineNum 
        while num > 99:
            passw += 1
            num = num - 100
    else:
    #we decrease
        num = num - lineNum
        while num < 0:
            if num + lineNum != 0:
                passw += 1
            num = 100 + num
        if num == 0:
            passw += 1


    line = file.readline()

print(passw)

file.close()