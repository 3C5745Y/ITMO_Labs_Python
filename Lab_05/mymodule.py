from random import randint
import time

sum1 = 0
sum2 = 0


def InputGamer():
    ig1 = input('Введите имя 1-го играющего ')
    ig2 = input('Введите имя 2-го играющего ')
    return (ig1, ig2)


def startGame(ig1, ig2):
    # Моделирование бросания кубика первого игрока
    sum1 = 0
    for i in range(5):
        print('Кубик бросает', ig1)
        time.sleep(2)
        n1 = randint(1, 6)
        print('Выпало: ', n1)
        sum1 += n1

    # Моделирование бросания кубика первого игрока
    sum2 = 0
    for i in range(5):
        print('Кубик бросает', ig2)
        time.sleep(2)
        n2 = randint(1, 6)
        print('Выпало: ', n2)
        sum2 += n2

    print(whoChampion(sum1, sum2, ig1, ig2))


def whoChampion(sum1, sum2, ig1, ig2):
    if sum1 > sum2:
        return ('Выиграл {0}, кол-во очков: {1}'.format(ig1, sum1))
    elif sum1 < sum2:
        return ('Выиграл {0}, кол-во очков: {1}'.format(ig2, sum2))
    else:
        return 'Ничья!'
