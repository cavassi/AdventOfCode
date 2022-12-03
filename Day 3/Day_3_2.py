with open('Day 3/data.txt', 'r') as file:
    line = file.read()

rucksack = line.rstrip().split("\n")

a = [chr(i) for i in range(ord('a'),ord('z')+1)]
b = []
for i in a:
    b.append(i.upper())

priority_values = a + b

def divide_into_groups_of_three(rucksack):
    divided_list = []
    finished_list = []
    for i in range(1, len(rucksack)+1):
        divided_list.append(rucksack[i-1])
        if i % 3 == 0:
            finished_list.append(divided_list)
            divided_list = []
    return finished_list

list = divide_into_groups_of_three(rucksack)

sum = 0
for group in list:
    for i in range(len(priority_values)):
        if priority_values[i] in group[0] and priority_values[i] in group[1] and priority_values[i] in group[2]:
            sum += i+1

print(sum)