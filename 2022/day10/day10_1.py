with open("day10/data.txt", "r") as data:
    data = data.read()

data = data.split("\n")

for i in range(len(data)):
    data[i] = data[i].split(" ")

# for i in range(len(data)):
#     print(data[i])

cycles = 0
sum = 1
total = 0

def check_sum_value(sum, total):
    if cycles == 20:
        total += (sum * cycles)
    elif cycles == 60:
        total += (sum * cycles)
    elif cycles == 100:
        total += (sum * cycles)
    elif cycles == 140:
        total += (sum * cycles)
    elif cycles == 180:
        total += (sum * cycles)
    elif cycles == 220:
        total += (sum * cycles)
    return total

for i in range(len(data)):
    if data[i][0] == "noop":
        cycles += 1
        total = check_sum_value(sum, total)
        continue
    else:
        cycles += 1
        total = check_sum_value(sum, total)
        cycles += 1
        total = check_sum_value(sum, total)
        sum += int(data[i][1])

print(total)