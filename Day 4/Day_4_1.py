with open('Day 4/data.txt', 'r') as file:
    line = file.read()

line = line.split("\n")
for i in range(len(line)):
    line[i] = line[i].split(",")

sum = 0

for i in range(len(line)):
    line[i][0] = line[i][0].split("-")
    line[i][1] = line[i][1].split("-")

print(line)
equals = 0

for i in range(len(line)):
    if line[i][0][0] <= line[i][-1][0] and line[i][0][-1] >= line[i][-1][-1]:
        sum += 1
    if line[i][0][0] == line[i][-1][0] and line[i][0][-1] == line[i][-1][-1]:
        equals += 1
    
for i in range(len(line)):
    if line[i][-1][0] <= line[i][0][0] and line[i][-1][-1] >= line[i][0][-1]:
        sum += 1

print(sum-equals)