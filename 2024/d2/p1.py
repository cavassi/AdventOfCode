input = "d2/data.txt"
test = "d2/test.txt"

reports = []
safe_reports = 0

with open(input, 'r') as data:
    for line in data:
        line = [int(i) for i in line.split()]
        reports.append(line)

def is_safe(report):
    sorted_report = sorted(report)
    reversed_sorted = list(reversed(sorted_report))

    if report == sorted_report or report == reversed_sorted:
        for i in range(len(report)-1):
            if abs(report[i] - report[i+1]) < 4 and report[i] != report[i+1]:
                continue
            else:
                return 0
    else:
        return 0 
    return 1


for line in reports:
    safe_reports += is_safe(line)

print(safe_reports)