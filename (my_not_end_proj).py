import random
import math

dictionary_of_all_message_on_diff_language = {
    "welcome": {
        "en": "Hello my dear friend!\nDO YOU WANT TO PLAY A GUESSING GAME?\nprint «YES» or «NO»: ",
        "ru": "Привет, мой дорогой друг!\nХОТИТЕ ПОИГРАТЬ В УГАДАЙКУ?\nНапечатайте «ДА» или «НЕТ»:"
    },
    "game_start_txt": {
        "en": "Welcome to the guessing game!\nYour task is to guess the number that was guessed using hints.",
        "ru": "Добро пожаловать в игру-угадайку!\nВаша задача — с помощью подсказок угадать число."
    },
    "choose_of_hard_lvl": {
        "en": "You can choose a difficulty level, which affects the range within which a given number may appear.",
        "ru": "Вы можете выбрать уровень сложности, который влияет на диапазон, в котором может оказаться данное число."
    },
    "lvl_type": {
        "en": "Levels are ranged from 1 to 5, which correspond to powers of ten as the maximum number in the range",
        "ru": "Уровни ранжируются от 1 до 5, которые соответствуют степени десятки = максимальному числу из диапазона"
    },
    "lvl_1": {
        "en": "You have selected level 1",
        "ru": "Вы выбрали уровень 1"
    },
    "lvl_2": {
        "en": "You have selected level 2",
        "ru": "Вы выбрали уровень 2"
    },
    "lvl_3": {
        "en": "You have selected level 3",
        "ru": "Вы выбрали уровень 3"
    },
    "lvl_4": {
        "en": "You have selected level 4",
        "ru": "Вы выбрали уровень 4"
    },
    "lvl_5": {
        "en": "You have selected level 5",
        "ru": "Вы выбрали уровень 5"
    },
    "enter_num": {
        "en": "Enter the number: ",
        "ru": "Введите число: "
    },
    "bigger": {
        "en": "The number is small. Try again: ",
        "ru": "Число мало. Попробуйте еще: "
    },
    "lower": {
        "en": "The number is large. Try again: ",
        "ru": "Число велико. Попробуйте еще: "
    },
    "range": {
        "en": "You are out of range.",
        "ru": "Вы вышли за диапазон."
    },
    "true/false": {
        "en": "Are you sure about your choice?(YES/NO): ",
        "ru": "Вы уверены в выборе?(ДА/НЕТ): "
    },
    "win_txt": {
        "en": "Congratulations! You won!",
        "ru": "Поздравляю! Вы победили!"
    },
    "best_way": {
        "en": "Algorithm result and number of moves: ",
        "ru": "Результат алгоритма и количество ходов: "
    },
    "exit_txt": {
        "en": "Exit?: ",
        "ru": "Выйти?: "
    }
}

def bin_search(num, sec_num):
    lt = list(range(0, 10 ** num + 1))
    low = 0
    high = len(lt) - 1
    #Цикл бинарного поиска
    while low <= high:
        mid = (low + high)/2
        ans = lt[mid]
        if ans == sec_num:
            return list[mid]
        if ans > sec_num:
            high = mid - 1
        else:
            low = mid + 1
    return None


def game_process(language, sec_num, st):
    num = -1
    while num != sec_num:
        num = int(input(print("enter_num", language)))
        if num > sec_num:
            print("bigger", language)
        elif num < sec_num:
            print("lower", language)
        elif num < 0 or num > 10**st:
            print("range", language)
        else:
            print("win_txt", language)
            print("best_way", language, bin_search(st, sec_num), math.log2(10**st))




def new_game(language):
    #Краткое текстовое описание
    print("game_start_txt", language)
    print("choose_of_hard_lvl", language)
    num = int(input(print("lvl_type", language)))
    #Выбор уровня игры
    if num == 1:
        sec_num = random.randint(0, 10**num)
        print("lvl_1", language)
        game_process(language, sec_num, num)
    elif num == 2:
        sec_num = random.randint(0, 10**num)
        print("lvl_2", language)
        game_process(language, sec_num, num)
    elif num == 3:
        sec_num = random.randint(0, 10**num)
        print("lvl_3", language)
        game_process(language, sec_num, num)
    elif num == 4:
        sec_num = random.randint(0, 10**num)
        print("lvl_4", language)
        game_process(language, sec_num, num)
    elif num == 5:
        sec_num = random.randint(0, 10**num)
        print("lvl_5", language)
        game_process(language, sec_num, num)
    else:
        return 0


def main():

    #Создание необходимых переменных
    exit_token = 0

    while exit_token != -1:
        #Модуль выбора языка
        language = input("Choose a language('ru' or 'en'): ").strip().lower()
        if language == 'ru':
            print("You have chosen Russian")
            if input(dictionary_of_all_message_on_diff_language["true/false"][language]).strip().upper() == "ДА":
                language = "ru"
                exit_token = -1
            else:
                continue
        elif language == 'en':
            print("You have chosen English")
            if input(dictionary_of_all_message_on_diff_language["true/false"][language]).strip().upper() == "YES":
                language = 'en'
                exit_token = -1
            else:
                continue
        else:
            continue

        #Модуль начала запуска игры
        if input(dictionary_of_all_message_on_diff_language["welcome"][language]).strip().upper() == "YES" or "ДА":
            new_game(language)
        else:
            continue
        if input(dictionary_of_all_message_on_diff_language["exit_txt"][language]) == "YES" or "ДА":
            return main()
        else:
            return 0

main()

