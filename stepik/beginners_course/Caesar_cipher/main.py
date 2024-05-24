def is_encryption(txt, lg, st):
    m = 26 if lg == '1' else 32
    txt2 = ''
    list_char = en if lg == '1' else ru
    for i in range(len(txt)):
        cur_idx = list_char.find(txt[i])
        if cur_idx != -1:
            idx = (list_char.find(txt[i]) + st) % m
            if txt[i].isupper():
                idx += 26 if lg == '1' else 32
            txt2 += list_char[idx]
        else:
            txt2 += txt[i]

    return txt2


def is_decryption(txt, lg, st):
    m = 26 if lg == '1' else 32
    txt2 = ''
    list_char = en if lg == '1' else ru
    for i in range(len(txt)):
        cur_idx = list_char.find(txt[i])
        if cur_idx != -1:
            idx = (list_char.find(txt[i]) - st) % m
            if txt[i].isupper():
                idx += 26 if lg == '1' else 32
            txt2 += list_char[idx]
        else:
            txt2 += txt[i]

    return txt2


def is_inp(txt):
    while True:
        res = input(txt)
        if res == '1' or res == '2':
            return res
        else:
            print("Введите 1 или 2")


ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
en = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def vruc():
    action = is_inp("Расшифровываем (1) или шифруем(2)? --->")
    lang = is_inp("Какой язык текста? English (1) или русский? (2)? --->")

    while True:
        step = input("Введите шаг сдвига --->")
        if step.isdigit():
            step = int(step)
            break
        else:
            print("Введите целое число")

    text = input("Введите нужную строку\n")

    if action == "1":
        text2 = is_decryption(text, lang, step)
    else:
        text2 = is_encryption(text, lang, step)

    print(text2)


def auto_encr():
    str = input("Введите текст для расшифровки\n")
    lang = is_inp("Какой язык текста? English (1) или русский? (2)? --->")
    max_step = 26 if lang == '1' else 32

    for i in range(1, max_step):
        print(is_decryption(str, lang, i))
        stop = input("Продолжаем? ('enter' - да. 'Не пустая строка' - нет-->")
        if stop != "":
            print("Шаг сдвига =", i)
            return


def super_encr():
    lang = '1'
    text = input("Введите строку для шифрования\n")
    text2 = ""
    tmp_text = ''
    for i in range(len(text)):
        if text[i] in en:
            tmp_text += text[i]
            if i == len(text)-1:
                text2 += (is_encryption(tmp_text, lang, len(tmp_text)))
        elif tmp_text != "":
            text2 += (is_encryption(tmp_text, lang, len(tmp_text))) + text[i]
            tmp_text = ""
        else:
            text2 += text[i]
    print(text2)


asd = input("Нужна автоматическая расшифровка (2) или ручная настройка (1) или супер-шифровка (3)?--->")
if asd == '1':
    vruc()
elif asd == '2':
    auto_encr()
elif asd == '3':
    super_encr()
else:
    print("Вы ввели что-то не то")

# Vq dg, qt oqrw vq dg, xlex ku wkh ycmabqwv
# Vq dg, qt oqrw vq dg, xlex ku wkh ycmabqwv
