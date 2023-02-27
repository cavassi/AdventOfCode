with open('day3/data.txt', 'r') as file:
    line = file.read()

rucksack = line.rstrip().split("\n")

a = [chr(i) for i in range(ord('a'),ord('z')+1)]
b = []
for i in a:
    b.append(i.upper())

priority_values = a + b

def divide_into_two_lists(items):
    first_compartment = []
    second_compartment = []
    backpack = []
    for i in range(int(len(items)/2)):
        first_compartment.append(items[i])
    for i in range(int((len(items)/2)), len(items)):
        second_compartment.append(items[i])
    backpack.append(first_compartment)
    backpack.append(second_compartment)
    return backpack

sum = 0
for elf in rucksack:
    backpack = divide_into_two_lists(elf)
    for i in range(len(priority_values)):
        if priority_values[i] in backpack[0] and priority_values[i] in backpack[1]:
            sum += i+1

print(sum)