# Задача: компьютер загадывает число от 1 до 100, нужно угадать его за минимальное количество попыток.
# В программе представлено три функции. Функции game_core_v1 и game_core_v2 были даны по условию.
# game_core_v3 - это улучшенная версия, которая угадывает число за меньшее количество попыток.

import numpy as np


def game_core_v1(number):
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


def game_core_v2(number):
    """Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его
       в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count  # выход из цикла, если угадали


def game_core_v3(number):
    """Используем метод бинарного поиска. Сначала берем число, равное середине интервала, если загаданное число
    меньше, то переходим в первую половину интервала, если больше - во вторую. И снова выбираем число, равное
    середине интервала. Продолжаем поиск до тех пор, пока не угадаем нужное число.
    Функция принимает загаданное число и возвращает число попыток"""

    count = 1  # счётчик количества попыток
    lower = 0  # нижняя граница интервала
    upper = 101  # верхняя граница интервала
    predict = upper // 2  # предполагаемое число

    while number != predict:
        count += 1
        if number > predict:
            lower = predict
            predict += (upper - predict) // 2
        elif number < predict:
            upper = predict
            predict -= (predict - lower) // 2
    return count


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Алгоритм функции {game_core} угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v1)
score_game(game_core_v2)
score_game(game_core_v3)
