print("Добро пожаловать, я робот шифровальщик.")


def cipher():
    text = input("Введите сообщение: ")
    n = len(text)
    print("     Ключ - перестановка чисел\n     Вам нужно ввести числа от 0 до", n-1, "\n     Например для текста из 4 символов подойдет ключ 1 3 0 2")
    key = input("Введите ключ: ")
    k = key.split(" ")
    new = ""
    for i in range(n):
        new += str(text[int(k[i])])
    print(new)


print("     Вот что я умею:\n     1 - зашифровать\n     2 - расшифровать")
move = int(input("Пожалуйста, выберите действие: "))
if move == 1:
    cipher()
else:
    print(1)

text = 0





