"""
The programm slovar.py
"""
import pyttsx3
engine = pyttsx3.init()

lis = []

def str_(st, k):
    count = k
    mes = []
    while True:
        if st[count] != ' ':
            mes.append(st[count])
            count += 1
        else:
            break
    return "".join(mes)

def check_words(s):
    count = 0
    n_count = 1
    while True:
        k = s.find(word, count)
        if k == -1:
            break
        print(n_count, ".", str_(s, k))
        count = k+1
        n_count += 1


if __name__=='__main__':

    with open('ru_listx') as file:
        for i in file:
            lis.append(i.strip('\t$123456789\n)'))

    while True:
        word = str(input("Введите слово для поиска в базе данных: "))
        if word == 'quit':
            break
        string_words = " ".join(lis)
        check_words(string_words)
        print("всего совпадений слов: ", string_words.count(word))


