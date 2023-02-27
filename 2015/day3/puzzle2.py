with open("day3/data.txt", "r") as data:
    data = data.read()

santa_location = [0,0]
robot_location = [0,0]
list_of_houses = [(0,0)]
a = False

for i in range(len(data)):
    a = False
    if i % 2 == 0:
        if data[i] == "^":
            santa_location[1] += 1
        if data[i] == ">":
            santa_location[0] += 1
        if data[i] == "v":
            santa_location[1] += -1
        if data[i] == "<":
            santa_location[0] += -1
        for k in range(len(list_of_houses)):
            if (santa_location[0] == list_of_houses[k][0] and \
                santa_location[1] == list_of_houses[k][1]):
                a = True
                break
    elif i % 2 != 0:
        if data[i] == "^":
            robot_location[1] += 1
        if data[i] == ">":
            robot_location[0] += 1
        if data[i] == "v":
            robot_location[1] += -1
        if data[i] == "<":
            robot_location[0] += -1
        for l in range(len(list_of_houses)):
            if (robot_location[0] == list_of_houses[l][0] and \
                robot_location[1] == list_of_houses[l][1]):
                a = True
                break

    if a == True:
        continue
    else:
        if i % 2 == 0:
            list_of_houses.append(tuple(santa_location))
        else:
            list_of_houses.append(tuple(robot_location))

print(len(list_of_houses))