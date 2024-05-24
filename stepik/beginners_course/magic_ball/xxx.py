import random

# приветствие
print("Добро пожаловать в числовую угадайку!")


def is_valid(num, granica):  # проверка числа на число и границы
    if num.isdigit():
        num = int(num)
        granica = int(granica)
        if 1 <= num <= granica:
            return True
        else:
            return False
    else:
        return False


def is_valid_2(granica):  # проверка границы на число и положительность
    if granica.isdigit():
        granica = int(granica)
        if 100 >= granica > 1:
            return True
        else:
            return False
    else:
        return False


while True: #доп.цикл для счетчика и возможности играть снова
    cnt = 0
    while True:  # запустили ввод границы и создали рандомное число
        g = input("Введите границу угадайки! Целое число больше единицы и до 100 включительно   ")
        if is_valid_2(g) == True:
            number = random.randint(1, int(g))
            break
        elif is_valid_2(g) == False:
            print("Попробуем еще раз :)")
            continue

    while True: #теперь угадываем число
        answer = input("Введите Ваше число   ")
        if not is_valid(answer, g):
            print("А может быть всё-таки введём целое число от 1 до", g)
            continue
        answer2 = int(answer)

        if answer2 < number:
            print("Ваше число меньше загаданного, попробуйте ещё разок :)")
            cnt += 1
            continue
        elif answer2 > number:
            print("Ваше число больше загаданного, попробуйте ещё разок :)")
            cnt += 1
            continue
        elif answer2 == number:
            print("Вы угадали! Поздравляем!!!")
            cnt += 1
        break

    print('И это всего-то c ', cnt, '-й попытки! Круто :)', sep='') #дали кол-во попыток

    answer3 = input("Хочешь поиграть ещё?    ") #возможность начать заново
    if answer3.lower() == "да":
        continue
    else:
        break

print("Спасибо, что играли в числовую угадайку! До скорых встреч ;)") #конец