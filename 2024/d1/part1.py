data = "2024/d1/data.txt"
test = "2024/d1/test.txt"

left_list = []
right_list = []

with open(data, 'r') as data:
    for line in data:
        line = line.split()
        left_list.append(int(line[0]))
        right_list.append(int(line[1]))

left_list = sorted(left_list)
right_list = sorted(right_list)

sum = 0

for i in range(len(left_list)):
    sum += (abs(right_list[i]-left_list[i]))

print(sum)
