with open("day3/data.txt", "r") as data:
    data = data.read()

location = [0,0]
list_of_houses = [(0,0)]
a = False

def check_if_in_list(location):
    if location in list_of_houses:
        return True
    else:
        return location

for i in range(len(data)):
    a = False
    if data[i] == "^":
        location[1] += 1
    if data[i] == ">":
        location[0] += 1
    if data[i] == "v":
        location[1] += -1
    if data[i] == "<":
        location[0] += -1

    for j in range(len(list_of_houses)):
        if location[0] == list_of_houses[j][0] and \
            location[1] == list_of_houses[j][1]:
            a = True
            break
    if a == True:
        continue
    else:
        list_of_houses.append(tuple(location))

print(len(list_of_houses))