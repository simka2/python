from random import randint, choice
from time import sleep


def is_print(answer_num, hid_num, cnt, right_border):
    """
    Функция выбирает одну из фраз для печати в процессе угадывания. Принимает введённое пользователем число,
    зааданное число, число попыток и правую границу. Возвращает 2 значения: False (если число не отгадано)
    или True (если отгадано) и строку для вывода на экран.
    """
    phrases_too_much = ['Ох, слишком много! Попробуй еще раз.', 'Многовато будет!', 'Ого-го, это слишком много!',
                        'Много!', 'Бери ниже', 'Многовато!', 'Нужно меньшее число!']
    phrases_too_little = ['Ох, слишком мало! Попробуй еще раз.', 'Маловато будет!', 'Эх, это слишком мало!',
                          'Мало!', 'Бери выше.', 'Маловато!', 'Нужно большее число!']
    phrases_almost = ['Почти угадал!', 'Горячо, но не очень.', 'Уже рядом', 'Ты близок.', 'Ты уже рядом.',
                      'Ну же, почти.', 'Горячо!']

    flag = True
    s = ""
    if answer_num > hid_num:
        if abs(answer_num - hid_num) < 5:
            s = choice(phrases_too_much) + " " + choice(phrases_almost)
        else:
            s = choice(phrases_too_much)
    elif answer_num < hid_num:
        if abs(answer_num - hid_num) < 5:
            s = choice(phrases_too_little) + " " + choice(phrases_almost)
        else:
            s = choice(phrases_too_little)
    if answer_num == hid_num:
        s = is_print_end(True, hid_num, right_border, cnt)
        flag = False
    return flag, s


def is_print_end(tp: bool, num: int, border: int, cnt: int):
    """
    Функция печатает конечный результат. На вход принимает bool (угадал, не угадал), загаданное число (int),
     правую границу диапазона (int) и число сделанных попыток (int)
    """
    phrases_guessed = ['Поздравляю! Ты угадал моё число :)', 'Молодец! Ты угадал :)', 'Ура, ты угадал! :)']
    phrases_too_soon = ['Ого, так быстро!', 'Да ты волшебник! Ты угадал моё число.', 'Скажи честно, ты подглядывал?',
                        'У тебя отличная интуиция!', 'Даже я бы не смог отгадать так быстро!']
    print("_" * 10)

    # Определяем нужный падеж.
    word = "попыток"
    if 1 < cnt % 10 < 5 and (cnt % 100 > 20 or cnt % 100 < 10):
        word = "попытки"
    if tp:
        if cnt <= 5:
            s = f"{choice(phrases_too_soon)} Поздравляю!"
        else:
            s = f"{choice(phrases_guessed)}\nТы угадал число {num} в интервале [1; {border}] за {cnt} {word}"
    else:
        s = f"Вы не угадали число {num} в интервале [1; {border}]. Вы сделали {cnt} {word}."
    s += "\nСпасибо, что играли в числовую угадайку. Еще увидимся..."
    s += "\n" + "_" * 50
    return s


def is_valid(n, right_border):
    if n.isdigit() and 0 < int(n) <= right_border:
        return True
    return False


def is_guess(right_border: int):
    """
    Функция угадывает число. На вход принимает целое число.
    """
    cnt = 0
    hidden_num = randint(1, right_border)
    while True:
        if cnt > 20:
            print(f"Это {cnt} попытка. Если желаете сдаться, наберите \"-1\".")
        otvet_users = input(f"Введите целое число от 1 до {right_border}: ")
        if is_game_exit(otvet_users):
            print(is_print_end(False, hidden_num, right_border, cnt))
            sleep(1)
            return
        if not is_valid(otvet_users, right_border):
            print(f"А может быть все-таки введем целое число от 1 до {right_border}?")
        else:
            otvet_users = int(otvet_users)
            cnt += 1
            go, st = is_print(otvet_users, hidden_num, cnt, right_border)
            if go:
                print(st)
                sleep(1)
            else:
                print(st)
                sleep(1)
                return
        print()


def is_game():
    """
    Функция позволяет изменить правую границу угадываемого интервала. А затем инициализирует игру.
    """
    st = ""
    while st == "":
        rule = """Правила:
            Компьютер загадывает число от 1 до 100 включительно. Ваша задача угадать его. Если желаете изменить 
            правую границу диапазона, то введите "0". В противном случае, просто нажмите \"Enter\"
            Выход - "-1".
        """
        print(rule)
        st = input("Начинаем игру? ")
        if is_game_exit(st):
            print("Конец игры")
            return

        right_border = 100
        if st == "0":
            while True:
                right_border = input("Введите новую правую границу диапазона: ")
                if is_game_exit(right_border):
                    print("Конец игры")
                    return
                if right_border.isdigit() and int(right_border) > 1:
                    right_border = int(right_border)
                    break
                else:
                    print("Вы должны ввести число больше 1. Для выхода введите \"-1\"")

            is_guess(right_border)

        if st == "":
            is_guess(right_border)
        sleep(0.1)
        st = input("Если желаете сыграть еще раз, нажмите \"Enter\". Если нет - введите что-нибудь. ")
    print("Конец игры.")


def is_game_exit(st: str):
    """
    Принимает строку. Если -1, то выводит True, иначе - False
    """
    if st == "-1":
        return True
    return False


print("Добро пожаловать в числовую угадайку!")
is_game()
