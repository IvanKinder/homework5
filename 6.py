my_dict = {}
digits = []
key = []

with open("lessons.txt") as les:
    lines = les.readlines()
    for line in lines:
        line = line.split(':')
        for i in range(len(line[1])):
            if line[1][i] == '\u2014':
                digits.append(0)
            if line[1][i] == ' ':
                if line[1][i + 1:i + 4].isdigit() or line[1][i + 1:i + 3].isdigit():
                    if line[1][i + 1:i + 4].isdigit():
                        digits.append(int(line[1][i + 1:i + 4]))
                    if line[1][i + 1:i + 3].isdigit() and line[1][i + 4].isalpha():
                        digits.append(int(line[1][i + 1:i + 3]))
        key.append(line[0])
    for i in range(0, int(len(digits)), 3):
        my_dict[key[int(i / 3)]] = sum(digits[i:i + 3])

print(my_dict)
