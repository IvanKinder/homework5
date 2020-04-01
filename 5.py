import random

numbers = [str(random.randint(0, 100)) for i in range(10)]
s = 0
my_list = []
with open("numbers.txt", "w") as num_file:
    for number in numbers:
        num_file.write(f'{number} ')

'''Упрощенный вариант'''
# for number in numbers:
#     s += int(number)
# print(s)
'''------конец-------'''

with open("numbers.txt") as re_file:
    for num in re_file.read().split():
        my_list.append(int(num))
print(sum(my_list))