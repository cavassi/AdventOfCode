with open("2015/day7/data.txt", "r") as data:
    data = data.read()

data = data.split("\n")

for i in range(len(data)):
    data[i] = data[i].split(" ")
    data[i].remove("->")

wire_dict = dict()

def get_value(key):
    if key.isdigit():
        return int(key)
    return wire_dict[key]

def NOT(line):
    key = line[1]
    value = get_value(key)
    result = ~value & 0xFFFF
    return result

def RSHIFT(line):
    key = line[0]
    value = get_value(key)
    result = value >> int(line[2])
    return result

def LSHIFT(line):
    key = line[0]
    value = get_value(key)
    result = value << int(line[2])
    return result

def OR(line):
    key1 = line[0]
    key2 = line[2]
    value1 = get_value(key1)
    value2 = get_value(key2)
    result = value1 | value2
    return result

def AND(line):
    key1 = line[0]
    key2 = line[2]
    value1 = get_value(key1)
    value2 = get_value(key2)
    result = value1 & value2
    return result

while len(data) > 1:
    for line in data:
        if len(line) == 2 and (line[0].isdigit() or line[0] in wire_dict):
            wire_dict[line[1]] = int(line[0])
            data.pop(data.index(line))

        if line[0] == "NOT" and line[1] in wire_dict:
            not_number = NOT(line)
            wire_dict[line[2]] = not_number
            data.pop(data.index(line))

        if line[0] in wire_dict and line[1] == "RSHIFT":
            rshift_number = RSHIFT(line)
            wire_dict[line[3]] = rshift_number
            data.pop(data.index(line))

        if line[0] in wire_dict and line[1] == "LSHIFT":
            lshift_number = LSHIFT(line)
            wire_dict[line[3]] = lshift_number
            data.pop(data.index(line))

        if line[0] in wire_dict and line[1] == "OR" and line[2] in wire_dict:
            or_number = OR(line)
            wire_dict[line[3]] = or_number
            data.pop(data.index(line))

        if (line[0] in wire_dict or line[0].isdigit()) and line[1] == "AND" and (line[2] in wire_dict or line[2].isdigit()):
            and_number = AND(line)
            wire_dict[line[3]] = and_number
            data.pop(data.index(line))          

print(wire_dict[data[0][0]])