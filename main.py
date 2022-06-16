file = open("switch.txt", "r")
data = file.readlines()[1:]
# ['switch01 te1/0 34241 133252\n', 'switch02 te2/0 22343433 522343342\n']
#split the list so we can recall individual line item
formatted_list = []
highest_talker = ""
max = 0
for i in range(len(data)):
    formatted_list.append(data[i].split())
# [['switch01', 'te1/0', '34241', '133252'], ['switch02', 'te2/0', '22343433', '522343342']]
for i in range(len(formatted_list)):
    each_list = formatted_list[i]
    # ['switch01', 'te1/0', '34241', '133252']
    for x in range(len(each_list)):
        total = int(each_list[2]) + int(each_list[3])
        if total > max:
            max = total
            highest_talker = each_list[0]

print(highest_talker)
print(max)
