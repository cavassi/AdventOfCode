with open('day1/data.txt', 'r') as file:
    line = file.read()

line = line.rstrip().split("\n\n")

current_value = 0
highest_value = 0
list_of_elfs = []

for elf in range(len(line)):
    line[elf] = line[elf].split("\n")

for i in range(len(line)):
    for j in range(len(line[i])):
        line[i][j] = int(line[i][j])

for elf in line:
    current_value = 0
    for food in elf:
        current_value += food
    list_of_elfs.append(current_value)

list_of_elfs.sort()
# dsd
print(list_of_elfs[-3] + list_of_elfs[-2] + list_of_elfs[-1])