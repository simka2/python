def tri(a, h):
    return 0.5 * h * a


def rect(a, b):
    return a * b


def circle(r):
    return 3.14 * r ** 2


def main():
    print("Начало модуля 1")

    print("Считаем площадь сложной фигуры")

    area = rect(20, 30) + tri(20, 15) + circle(5)
    print(f'{area = }')

    print("Конец модуля 1")

print(__name__)
if __name__ == '__main__':
    main()
