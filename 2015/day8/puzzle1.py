import copy

with open("2015/day8/data.txt", "r") as data:
    data = data.read()

data = data.split("\n")

for i in range(len(data)):
    data[i] = data[i].split("\n")

data_copy = copy.deepcopy(data)

total_characters = 0

for line in data:
    total_characters += len(line[0])
