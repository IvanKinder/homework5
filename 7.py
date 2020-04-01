import json

with open("firms.txt") as my_file:
    firms = [line for line in my_file.read().split()]
    money_free = {firms[i]: int(firms[i + 2]) - int(firms[i + 3]) for i in range(0, len(firms), 4)}
    all_money = 0
    i = 0
    for value in money_free.values():
        if value > 0:
            all_money += value
            i += 1
    mid_money = {"Средняя прибыль": all_money / i}
    my_dict = [money_free, mid_money]
    print(my_dict)
with open("json_list.json", "w") as j_file:
    json.dump(my_dict, j_file, ensure_ascii=False)
