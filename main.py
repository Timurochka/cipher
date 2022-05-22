def code(key, text):
    blocksize = len(key)
    n = len(text)
    block = ''
    code = ''
    for i in range(0, n, blocksize):
        block = [text[i + j] for j in range(blocksize)]
        for j in range(blocksize):
            code += block[key.index(j)]
    return code


def letter(key, text):
    blocksize = len(key)
    n = len(text)
    if n % blocksize != 0:
        for i in range(blocksize - (n % blocksize)):
            text += str("§")
    print(code(key, text))


def group(key, text):
    poskolko = int(input("По сколько символов нужно группировать? "))
    te_xt = [text[i:i+poskolko] for i in range(0, len(text), poskolko)]
    if len(te_xt[-1]) != poskolko:
        for i in range(poskolko - (len(te_xt[-1]) % poskolko)):
            te_xt[-1] += str("§")
    print(code(key, te_xt))


def word(key, text):
    blocksize = len(key)
    te_xt = text.split(" ")
    if len(te_xt) != blocksize:
        for i in range(blocksize - (len(te_xt) % blocksize)):
            te_xt.append("§"*5)
    n = len(te_xt)
    block = ''
    code = ''
    for i in range(0, n, blocksize):
        block = [te_xt[i + j] for j in range(blocksize)]
        for j in range(blocksize):
            code += block[key.index(j)]
            code += " "
    print(code)


def cipher():
    text = input("Введите сообщение: ")
    print("     Ключ - перестановка чисел, с помощью которой будет шифроваться ваш текст\n     Например, <<1 3 0 2>>")
    k = input("Введите ключ: ")
    ke = k.split()
    key = []
    for e in ke:
        key.append(int(e))
    print("     1 - посимвольное шифрование\n     2 - шифрование группы\n     3 - шифрование слов")
    how = int(input("Способ шифровки: "))
    if how == 1:
        letter(key, text)
    if how == 2:
        group(key, text)
    if how == 3:
        word(key, text)


def decode(key, text):
    blocksize = len(key)
    n = len(text)
    block = ''
    code = ''
    for i in range(0, n, blocksize):
        block = [text[i + j] for j in range(blocksize)]
        for j in range(blocksize):
            code += block[key.index(j)]
    code = code.replace("§", "")
    return code


def deletter(key, text):
    for i in range(len(key)//2):
        key[i], key[-i-1] = key[-i-1], key[i]
    print(decode(key, text))


def degroup(key, text):
    poskolko = int(input("По сколько символов было сгруппировано? "))
    te_xt = [text[i:i + poskolko] for i in range(0, len(text), poskolko)]
    for i in range(len(key)//2):
        key[i], key[-i-1] = key[-i-1], key[i]
    print(decode(key, te_xt))


def deword(key, text):
    te_xt = text.split()
    for i in range(len(key)//2):
        key[i], key[-i-1] = key[-i-1], key[i]
    blocksize = len(key)
    n = len(te_xt)
    block = ''
    code = ''
    for i in range(0, n, blocksize):
        block = [te_xt[i + j] for j in range(blocksize)]
        for j in range(blocksize):
            code += block[key.index(j)]
            code += " "
    code = code.replace("§", "")
    print(code)


def decipher():
    text = input("Введите зашиврованный текст: ")
    k = input("Введите ключ: ")
    ke = k.split(" ")
    key = []
    for e in ke:
        key.append(int(e))
    print("     1 - посимвольное шифрование\n     2 - шифрование группы\n     3 - шифрование слов")
    how = int(input("Способ шифровки: "))
    if how == 1:
        deletter(key, text)
    if how == 2:
        degroup(key, text)
    if how == 3:
        deword(key, text)


def start():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Добро пожаловать, я робот шифровальщик.")
    print("     Вот что я умею:\n     1 - зашифровать\n     2 - расшифровать")
    move = int(input("Пожалуйста, выберите действие: "))
    if move == 1:
        cipher()
    else:
        decipher()


while(True):

    start()
    text = 0
