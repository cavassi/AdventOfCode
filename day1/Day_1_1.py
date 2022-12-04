with open('Day 1/data.txt', 'r') as file:
    line = file.read()

line = line.rstrip().split("\n\n")

current_value = 0
highest_value = 0

for elf in range(len(line)):
    line[elf] = line[elf].split("\n")

for i in range(len(line)):
    for j in range(len(line[i])):
        line[i][j] = int(line[i][j])

for elf in line:
    current_value = 0
    for food in elf:
        current_value += food
    if current_value > highest_value:
        highest_value = current_value

print(highest_value)