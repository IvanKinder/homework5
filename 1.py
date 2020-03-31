with open("input.txt", "w") as file_1:
    while True:
        text = input("Введите что-нибудь и это запишется в файл: ")
        if text:
            file_1.write(text + "\n")
        else:
            break
