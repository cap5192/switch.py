file = open("switch.txt", "r")
data = file.readlines()
# [name, int, input ...],[switch01, te1/o, ..\n]...
formated_data = []
new_data = []
max = 0
highest_talker = ""
for i in data:
    formated_data.append(i.split())
# [[name, int..],[switch01, te1/0...]
for i in range(len(formated_data)):
    if i > 0:
        new_data.append(formated_data[i])
# [[switch01, te1/0, ..],[switch02...]

for i in range(len(new_data)):
    current_data = new_data[i]
    for x in range(len(current_data)):
        y = (int(current_data[2]) + int(current_data[3]))
        if y > max:
            max = y
            highest_talker = current_data[0]
print(f"Highest talker is {highest_talker} with total of {max} Bytes")

