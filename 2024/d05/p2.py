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

for list in page_updates:
    for i in range(len(list)):
        list[i] = int(list[i])

page_orders = {}

for pair in page_orders_raw:
    if pair[0] not in page_orders:
        page_orders.setdefault(pair[0],[])
    page_orders[pair[0]].append(pair[1])
   

incorrect_orders = []

for updates in page_updates:
    for index, number in enumerate(updates[:-1]):
        num_1 = int(number)
        num_2 = int(updates[index+1])

        if num_2 not in page_orders:
            continue

        if num_1 in page_orders[num_2]:
            incorrect_orders.append(updates)
            break

def checker(temp_updates, i):
    if temp_updates[i] not in page_orders:
        temp_updates[i], temp_updates[i+1] = temp_updates[i+1], temp_updates[i]
        return temp_updates    

    if temp_updates[i+1] not in page_orders:
        return temp_updates      

    if temp_updates[i] in page_orders[temp_updates[i+1]]:
        temp_updates[i], temp_updates[i+1] = temp_updates[i+1], temp_updates[i]
        return temp_updates
    
    if temp_updates[i+1] not in page_orders[temp_updates[i]]:
        temp_updates[i], temp_updates[i+1] = temp_updates[i+1], temp_updates[i]
        return temp_updates
    return temp_updates

correct_orders = []

for updates in incorrect_orders:
    temp_updates = updates.copy()
    for iteration in range(len(temp_updates)):
        for i in range(len(updates)-1):
            temp_updates = checker(temp_updates, i)
    correct_orders.append(temp_updates)

sum = 0

for list in correct_orders:
    sum += list[(len(list) // 2 ) ]

print(sum)