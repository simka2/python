def is_transfer_10(num, sys):
    degree = len(num) - 1
    sys = int(sys)
    new_num = 0
    for i in num:
        if i.isdigit():
            new_num += int(i) * sys ** degree
        else:
            if i == "A":
                i = '10'
            elif i == "B":
                i = '11'
            elif i == "C":
                i = '12'
            elif i == "D":
                i = '13'
            elif i == "E":
                i = '14'
            elif i == "F":
                i = '15'
            new_num += int(i) * sys ** degree
        degree -= 1
    return new_num


def is_num(str):
    while True:
        num = input(str)
        if num.isdigit():
            return num
        else:
            return num


def perevod(a):
    str = "Введите число-->"
    str2 = "Введите систему счисления-->"
    number = is_num(str)
    sys = is_num(str2)

    if a == '0':
        new_number = is_transfer_10(number, sys)
    elif a == '10':
        new_number = is_transfer_all(number, sys)
    print(new_number)


def uravn():
    nums = [88, 32, 22, 16, 17]
    nums10 = list()
    for i in range(5):
        nums10.append(is_transfer_10(str(nums[i]), 9))

    for i in range(1, len(nums10)):
        if i != len(nums10) - 1:
            print(nums10[i], end="+")
        else:
            print(nums10[i], end="=")
    print(nums10[0], sum(nums10) - nums10[0] == nums10[0])


def is_transfer_all(num, sys):
    list_d = []
    num = int(num)
    sys = int(sys)
    new_num = ''
    if sys - 1 >= num:
        return num
    else:
        while True:
            ost = num % sys
            list_d.append(ost)
            num = num // sys
            if num <= sys - 1:
                list_d.append(num)
                break

        for i in range(len(list_d) - 1, -1, -1):
            if len(str(list_d[i])) == 1:
                new_num += str(list_d[i])
            elif len(str(list_d[i])) == 2:
                if list_d[i] == 10:
                    new_num += 'A'
                if list_d[i] == 11:
                    new_num += 'B'
                if list_d[i] == 12:
                    new_num += 'C'
                if list_d[i] == 13:
                    new_num += 'D'
                if list_d[i] == 14:
                    new_num += 'E'
                if list_d[i] == 15:
                    new_num += 'F'

    return new_num


a = input("Перевод в ручную (1), уравнение с деревьями (2), из 10 в другую (3)--->")
if a == '1':
    perevod('0')
elif a == '2':
    uravn()
elif a == '3':
    perevod('10')
