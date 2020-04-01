with open("costs.txt") as file_1:
    people = file_1.read().split()
    my_dict = {}

    for i in range(0, len(people) - 1, 2):
        my_dict[people[i]] = float(people[i + 1])

    print("Сотрудники, имеющие заработную плату менее 20000: ")
    for key, value in my_dict.items():
        if value < 20000:
            print(key)
        s = sum((my_dict.values()))
        people_count = len(my_dict.values())
    print(f"Средний доход сотрудников: {s / people_count :.2f}")
