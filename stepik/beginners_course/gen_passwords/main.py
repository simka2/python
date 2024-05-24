from random import choice, randint


def validat(char: str, value: str):
    """
    Прнимает 2 строки. В char лежит "dig" (ожидается число) или "st" (строка).
    Проверяет правильность значений и возвращает False (если значения не прошли проверку) или число или строку.
    """
    char = char.split("_")
    good_val = ["да", "1", "нет", "0"]
    if char[0] == 'st':
        if value == "да" or value == '1':
            return '1'
        elif value == 'нет' or value == '0':
            return '0'
        else:
            return False
    elif char[0] == 'dig':
        if char[1] == '20' and value.isdigit():
            if 1 <= int(value) <= 20:
                return int(value)
            else:
                return False
        elif char[1] == "30" and value.isdigit():
            if 4 <= int(value) <= 30:
                return int(value)
            else:
                return False
        elif char[1] == '0' and value.isdigit():
            if 0 <= int(value) <= 1:
                return value  # Возвращаем '1' или '0'
            else:
                return False
        else:
            return False
    else:
        return False


def gen_str_char(dig, up_word, low_word, spec_char, bad_char):
    """
    Генерирует строку, из которой будет собираться пароль. Получает строки, возвращает лист строк.
    """
    list_char = []
    if dig == '1':
        list_char.extend(num)
    if up_word == '1':
        list_char.extend(ucase)
    if low_word == '1':
        list_char.extend(lcase)
    if spec_char == "1":
        list_char.extend(special)
    if bad_char == '0':  # Тут всё верно. 0 - значит исключить. 1 - значит не исключать.
        list_char.extend(al)

    return list_char


def gen_pass(nums, len_min, len_max, list_chars):
    list_pass = list()
    for _ in range(nums):
        pas = ''
        for j in range(randint(len_min, len_max)):
            pas += choice(list_chars)
        list_pass.append(pas)

    return list_pass


def vvod():
    """
    Запрашивает у пользователя данные. Если что-то не так, возвращает False, иначе True
    """

    quan = input(f"Количество паролей для генерации?\n").split()
    if len(quan) == 1:
        quantity = validat("dig_20", quan[0])
    elif len(quan) == 3:
        quantity = validat("dig_20", quan[0])
        len_pass = quan[1].split("-")
        if len(len_pass) == 1:
            len_pass_min = len_pass_max = validat("dig_20", len_pass[0])
        elif len(len_pass) == 2:
            len_pass_min = validat("dig_30", len_pass[0])
            len_pass_max = validat("dig_30", len_pass[1])
        else:
            return False
        bad_char = validat("dig_0", quan[2])
        if not (quantity and len_pass_min and len_pass_max and bad_char):
            return False
        str_char_pass = gen_str_char('1', '1', '1', '1', bad_char)
        list_passord = gen_pass(quantity, len_pass_min, len_pass_max, str_char_pass)

        return list_passord
    else:
        return False

    len_pass = input(f"Длина пароля? (можно ввести строку 'min-max', где min - мин длина, max - макс длина)\n").split(
        "-")
    if len(len_pass) == 1:
        len_pass_min = len_pass_max = validat("dig_30", len_pass[0])
    elif len(len_pass) == 2:
        len_pass_min = validat("dig_30", len_pass[0])
        len_pass_max = validat("dig_30", len_pass[1])
    else:
        return False

    dig = input(f"Включать ли цифры? {num}\n").lower()
    dig = validat("st", dig)

    up_word = input(f"Включать ли прописные буквы? {ucase}\n").lower()
    up_word = validat("st", up_word)

    low_word = input(f"Включать ли строчные буквы? {lcase}\n").lower()
    low_word = validat("st", low_word)

    spec_char = input(f"Включать ли спец. символы? {special}\n").lower()
    spec_char = validat("st", spec_char)

    bad_char = input(f"Исключать ли неоднозначные символы? {al}\n").lower()
    bad_char = validat("st", bad_char)

    if not (quantity and len_pass_min and len_pass_max and dig and up_word and low_word and spec_char and bad_char):
        return False
    str_char_pass = gen_str_char(dig, up_word, low_word, spec_char, bad_char)
    list_passord = gen_pass(quantity, len_pass_min, len_pass_max, str_char_pass)

    return list_passord


num = '23456789'
lcase = 'abcdefghjkmnpqrstuvwxyz'
ucase = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
special = '!#$%&*+-=?@^_'
al = 'il1Lo0O'

st = """Генерация паролей. Можешь ввести строку вида
    quantity lenght al
    где quantity - число паролей (целое число. Не должно превышать 20).
    lenght - длина паролей. Целое число (не должно превышать 30 и должно быть больше 3) или строка вида 12-20 (диапазон длин 
    от 12 до 20 включительно)
    al - исключаем ли неоднозначные символы (il1Lo0O) (1 - исключаем, 0 - оставляем)
    Пример: 10 8-12 1 или 10 8 12
    или можешь просто отвечать на вопросы, вводя да/1 или нет/0
    """

print(st)
lst_pass = vvod()
if not lst_pass:
    print("Не верно введена строка.")
else:
    print(*lst_pass, sep="\n")
