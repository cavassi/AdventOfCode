with open('day4/data.txt', 'r') as file:
    line = file.read()

line = line.split("\n")

for i in range(len(line)):
    line[i] = line[i].split(",")
    line[i][0] = line[i][0].split("-")
    line[i][1] = line[i][1].split("-")

sum = 0

for i in range(len(line)):
    if int(line[i][0][0]) <= int(line[i][-1][0]) and int(line[i][0][-1]) >= int(line[i][-1][0]):
        sum += 1
        continue
    elif int(line[i][-1][0]) <= int(line[i][0][0]) and int(line[i][-1][-1]) >= int(line[i][0][0]):
        sum += 1
print(sum)