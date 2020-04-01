with open("lines.txt") as my_file:
    lines = my_file.read().split("\n")
    print(f"Количество строк в файле = {len(lines)}")
    for line in enumerate(lines, 1):
        print(f"Количество слов в {line[0]} строке равно: {len(line[1].split())}")
