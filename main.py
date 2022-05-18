import random

print("Добро пожаловать, я робот шифровальщик.")


def letter(k, text):
    blocksize = len(k)
    n = len(text)
    if n % blocksize != 0:
        for i in range(blocksize - (n % blocksize)):
            text += str(chr(random.randrange(ord('a'), ord('z'), 1)))
    n = len(text)
    new = ''
    code = ''
    for i in range(0, n, blocksize):
        new = [text[i+j] for j in range(blocksize)]
        for j in range(blocksize):
            code += str(new[blocksize - int(k[j]) - 1])
    print(code)

def group(k, text):


def cipher():
    text = input("Введите сообщение: ")
    print("     Ключ - перестановка чисел, с помощью которой будет шифроваться ваш текст\n     Например, <<1 3 0 2>>")
    key = input("Введите ключ: ")
    k = key.split(" ")
    print("     1 - посимвольное шифрование\n     2 - шифрование группы\n     3 - шифрование слов")
    how = int(input("Способ шифровки: "))
    if how == 1:
        letter(k, text)
    if how == 2:
        group(k, text)

print("     Вот что я умею:\n     1 - зашифровать\n     2 - расшифровать")
move = int(input("Пожалуйста, выберите действие: "))
if move == 1:
    cipher()
else:
    pass

text = 0





