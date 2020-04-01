with open("text4.txt") as r_file:
    my_words = r_file.read().split()
    i = 0
    keys_rus = ['Один ', 'Два ', 'Три ', 'Четыре ']
    for word in my_words:
        if word.isalpha():
            my_words.insert(my_words.index(word), keys_rus[i])
            my_words.remove(word)
            i += 1

with open("text4_rus.txt", "w") as w_file:
    for i in range(1, len(my_words) + 1):
        if i % 3 == 0:
            w_file.write(f' {my_words[i - 1]}')
            w_file.write('\n')
        else:
            w_file.write(my_words[i - 1])
