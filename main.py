file = open("switch.txt", "r")
data = file.readlines()
each_line = []
max = 0
highest_talker = ""
for i in range(len(data)):
    if i > 0:
        each_line.append(data[i].split())
for i in range(len(each_line)):
    one_line = each_line[i]
    for x in range(len(one_line)):
        total = int(one_line[2]) + int(one_line[3])
        if total > max:
            max = total
            highest_talker = one_line[0]

print(f"Highest talker switch is {highest_talker} with total usage of {max}")

