input = "2024/d05/data.txt"
test = "2024/d05/test.txt"

raw_data = []
sum = 0

with open(input, 'r') as data:
    for line in data:
        raw_data.append(line)

page_orders_raw = []
page_updates = []

for line in raw_data:
    if "|" in line:
        line = line.strip().split("|")
        line = [int(line[0]), int(line[1])]
        page_orders_raw.append(line)

    if "," in line:
        page_updates.append(line.strip().split(","))

page_orders = {}

for pair in page_orders_raw:
    if pair[0] not in page_orders:
        page_orders.setdefault(pair[0],[])
    page_orders[pair[0]].append(pair[1])

for key, value in page_orders.items():
    print(key,value)    

for updates in page_updates:
    for index, number in enumerate(updates[:-1]):
        num_1 = int(number)
        num_2 = int(updates[index+1])

        if num_2 not in page_orders:
            continue

        if num_1 in page_orders[num_2]:
            correct = False
            break
        correct = True
    if correct:
        sum += int(updates[len(updates) // 2])

print(sum)