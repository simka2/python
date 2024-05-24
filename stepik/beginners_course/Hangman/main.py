from random import choice
import os

word_list = ['Абрикос', 'айва', 'апельсин', 'арбуз', 'банан', 'виноград', 'гранат', 'грейпфрут', 'груша', 'гуава',
             'дыня', 'инжир', 'канталупа', 'карамбола', 'киви', 'красный банан', 'лимон', 'манго', 'марания', 'мушмула',
             'пепино', 'персик', 'питайя', 'помело', 'физалис', 'финик', 'хурма']


def get_word():
    word = choice(word_list)
    return word


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     /|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def validate_char(st):
    ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    while True:
        if st.isalpha():
            if len(st) == 1:
                if st in ru:
                    return st
                else:
                    print("Вводите русские буквы")
                    st = input("Введите букву или слово целиком:\n").upper()
            else:
                return st
        else:
            print("Вы должны ввести букву.")
            st = input("Введите букву или слово целиком:\n").upper()


def validate(st, guessed_letters):
    while True:
        st = validate_char(st)
        if st in guessed_letters:
            if len(st) == 1:
                print(f"Буква {st} уже была")
            else:
                print(f"Слово {st} уже было")
            st = input("Введите новую букву или слово целиком\n").upper()
        else:
            return st


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    while True:
        clear = lambda: os.system('cls')
        clear()
        print('Давайте играть в угадайку слов!')
        print(display_hangman(tries))
        print(word_completion)
        if tries == 0:
            print(word)
            return
        char = validate(input("Введите букву или слово целиком:\n").upper(), guessed_letters)
        guessed_letters.append(char)
        if char == word:
            print("Поздравляем, вы угадали слово! Вы победили!")
            return
        elif len(char) == 1 and char in word:
            i = 0
            while word.find(char, i) != -1:
                i = word.find(char)
                word_completion = word_completion[:i] + char + word_completion[i + 1:]
                i += 1
        else:
            tries -= 1


while True:
    word = get_word().upper()
    play(word)
    a = input("Сыграем еще раз? (да = enter; нет=н или 0)---->")
    if a == '0' or a == 'н' or a == 'нет':
        break
print("Спасибо за игру!")
