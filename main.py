import random

print("Добро пожаловать, я робот шифровальщик.")


def code(k, text):
    blocksize = len(k)
    n = len(text)
    new = ''
    code = ''
    for i in range(0, n, blocksize):
        new = [text[i + j] for j in range(blocksize)]
        for j in range(blocksize):
            code += str(new[blocksize - int(k[j]) - 1])
    print(code)


def letter(k, text):
    blocksize = len(k)
    n = len(text)
    if n % blocksize != 0:
        for i in range(blocksize - (n % blocksize)):
            text += str("\0")
            # text += str(chr(random.randrange(ord('a'), ord('z'), 1)))
    code(k, text)


def group(k, text):
    poskolko = int(input("По сколько символов нужно группировать? "))
    te_xt = [text[i:i+poskolko] for i in range(0, len(text), poskolko)]
    if len(te_xt[-1]) != poskolko:
        for i in range(poskolko - (len(te_xt[-1]) % poskolko)):
            te_xt[-1] += str("\0")
    code(k, te_xt)


def word(k, text):
    blocksize = len(k)
    te_xt = text.split(" ")
    if len(te_xt) != blocksize:
        for i in range(blocksize - (len(te_xt) % blocksize)):
            te_xt.append("\0"*5)
    n = len(te_xt)
    new = ''
    code = ''
    for i in range(0, n, blocksize):
        new = [te_xt[i + j] for j in range(blocksize)]
        for j in range(blocksize):
            code += str(new[blocksize - int(k[j]) - 1])
            code += " "
    print(code)


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
    if how == 3:
        word(k, text)


def decode(k, text):
    blocksize = len(k)
    n = len(text)
    new = ''
    code = ''
    for i in range(0, n, blocksize):
        new = [text[i + j] for j in range(blocksize)]
        for j in range(blocksize):
            code += str(new[blocksize - int(k[j]) - 1])
    code = code.replace("\0", "")
    print(code)


def deletter(k, text):
    for i in range(len(k)//2):
        k[i], k[-i-1] = k[-i-1], k[i]
    decode(k, text)


#def degroup(k, text):


def deword(k, text):
    for i in range(len(k)//2):
        k[i], k[-i-1] = k[-i-1], k[i]
    blocksize = len(k)
    te_xt = text.split(" ")
    if len(te_xt) != blocksize:
        for i in range(blocksize - (len(te_xt) % blocksize)):
            te_xt.append("\0" * 5)
    n = len(te_xt)
    new = ''
    code = ''
    for i in range(0, n, blocksize):
        new = [te_xt[i + j] for j in range(blocksize)]
        for j in range(blocksize):
            code += str(new[blocksize - int(k[j]) - 1])
            code += " "
    code = code.replace("\0", "")
    print(code)


def decipher():
    text = input("Введите зашиврованный текст: ")
    key = input("Введите ключ: ")
    print("     1 - посимвольное шифрование\n     2 - шифрование группы\n     3 - шифрование слов")
    how = int(input("Способ шифровки: "))
    k = key.split(" ")
    if how == 1:
        deletter(k, text)
    if how == 2:
        degroup(k, text)
    if how == 3:
        deword(k, text)


print("     Вот что я умею:\n     1 - зашифровать\n     2 - расшифровать")
move = int(input("Пожалуйста, выберите действие: "))
if move == 1:
    cipher()
else:
    decipher()

text = 0





