with open("day3/data.txt", "r") as data:
    data = data.read()

location = [0,0]
list_of_houses = [0,0]

for i in range(len(data)):
    if data[i] == "^":
        location[1] += 1
    if data[i] == ">":
        location[0] += 1
    if data[i] == "v":
        location[1] += -1
    if data[i] == "<":
        location[0] += -1
    
    for j in range(len(list_of_houses)):
        if location not in list_of_houses:
            list_of_houses.append(location)

print(list_of_houses)