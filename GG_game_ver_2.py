import random
import sys

dictionary_of_all_message_on_diff_language = {
    "welcome": {
        "en": "Hello my dear friend!\nDO YOU WANT TO PLAY A GUESSING GAME?\nPrint «YES» or «NO»: ",
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
        "en": "Levels are ranged from 1 to 5, which correspond to powers of ten as the maximum number in the range: ",
        "ru": "Уровни ранжируются от 1 до 5, которые соответствуют степени десятки = максимальному числу из диапазона: "
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
        "en": "Exit?(YES/NO): ",
        "ru": "Выйти?(ДА/НЕТ): "
    }
}


def bin_search(num, sec_num):
    col = 0
    lt = list(range(0, 10 ** num + 1))
    low = 0
    high = len(lt) - 1
    # Цикл бинарного поиска
    while low <= high:
        col += 1
        mid = (low + high) // 2  # Целочисленное деление
        ans = lt[mid]
        if ans == sec_num:
            return ans, col
        if ans > sec_num:
            high = mid - 1
        else:
            low = mid + 1
    return None, col


def int_value(line):
    while True:
        check = input(line.strip())
        try:
            return int(check)
        except ValueError:
            print("Error!")


def game_process(language, sec_num, st):
    num = -1
    while num != sec_num:
        num = int_value(dictionary_of_all_message_on_diff_language["enter_num"][language])
        if num < 0 or num > 10**st:
            print(dictionary_of_all_message_on_diff_language["range"][language])
        elif num < sec_num:
            print(dictionary_of_all_message_on_diff_language["bigger"][language])
        elif num > sec_num:
            print(dictionary_of_all_message_on_diff_language["lower"][language])
        else:
            print(dictionary_of_all_message_on_diff_language["win_txt"][language])
            print(dictionary_of_all_message_on_diff_language["best_way"][language], bin_search(st, sec_num))


def new_game(language):
    #Краткое текстовое описание
    print(dictionary_of_all_message_on_diff_language["game_start_txt"][language])
    print(dictionary_of_all_message_on_diff_language["choose_of_hard_lvl"][language])
    num = abs(int_value(dictionary_of_all_message_on_diff_language["lvl_type"][language]))
    #Выбор уровня игры
    while num != -1:
        if num == 1:
            sec_num = random.randint(0, 10**num)
            print(dictionary_of_all_message_on_diff_language["lvl_1"][language])
            game_process(language, sec_num, num)
            num = -1
        elif num == 2:
            sec_num = random.randint(0, 10**num)
            print(dictionary_of_all_message_on_diff_language["lvl_2"][language])
            game_process(language, sec_num, num)
            num = -1
        elif num == 3:
            sec_num = random.randint(0, 10**num)
            print(dictionary_of_all_message_on_diff_language["lvl_3"][language])
            game_process(language, sec_num, num)
            num = -1
        elif num == 4:
            sec_num = random.randint(0, 10**num)
            print(dictionary_of_all_message_on_diff_language["lvl_4"][language])
            game_process(language, sec_num, num)
            num = -1
        elif num == 5:
            sec_num = random.randint(0, 10**num)
            print(dictionary_of_all_message_on_diff_language["lvl_5"][language])
            game_process(language, sec_num, num)
            num = -1
        else:
            num = abs(int_value(dictionary_of_all_message_on_diff_language["lvl_type"][language]))
            continue


def check_of(txt, language):
    check = input(dictionary_of_all_message_on_diff_language[txt][language]).strip().upper()
    if check == "YES" or check == "ДА":
        return 1
    elif check == "NO" or check == "НЕТ":
        return -1
    else:
        print("Error!")
        return 0


def main():

    #Создание необходимых переменных
    exit_token = 0
    langauge = ''
    while exit_token != -1:
        #Модуль выбора языка
        language = input("Choose a language('ru' or 'en'): ").strip().lower()
        if language == 'ru':
            print("Вы выбрали русский язык.")
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
    exit_token = 0
    #Модуль начала запуска игры
    while exit_token != -1:
        res = check_of("welcome", language)
        if res == 1:
            new_game(language)
        elif res == -1:
            # Модуль выхода из игры
            while exit_token != -1:
                res = check_of("exit_txt", language)
                if res == 1:
                    sys.exit()
                elif res == -1:
                    return main()
                else:
                    continue
        else:
            continue


if __name__ == "__main__":
    main()

