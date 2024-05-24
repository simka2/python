# объявление функции
def is_pangram(text):
    text=text.lower()
    alf=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for c in alf:
        if c not in text:
            return False

# считываем данные


# вызываем функцию
print(is_pangram('Jackdaws love my big sphinx of quartz'))