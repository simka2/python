def input_name():
    return input("Введите имя: ").title()


def input_surname():
    return input("Введите фамилию: ").title()


def input_patronumic():
    return input("Введите отчество: ").title()


def input_phone():
    return input("Введите телефон: ")


def input_address():
    return input("Введите адрес: ").title()


def create_contact():
    surname = input_surname()
    name = input_name()
    patronumic = input_patronumic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronumic} {phone}\n{address}\n\n'