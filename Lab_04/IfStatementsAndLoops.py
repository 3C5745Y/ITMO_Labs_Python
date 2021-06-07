from random import randint
import time

#Ввод имен играющих
igrok1 = input('Введите имя 1-го игрока ')
igrok2 = input('Введите имя 2-го игрока ')


#Моделирование бросания кубика первого игрока
sum1 = 0
for i in range(5):
    print('Кубик бросает', igrok1)
    time.sleep(2)
    n1 = randint(1, 6)
    print('Выпало: ', n1)
    sum1 += n1


#Моделирование бросания кубика первого игрока
sum2 = 0;
for i in range(5):
    print('Кубик бросает', igrok2)
    time.sleep(2)
    n2 = randint(1, 6)
    print('Выпало: ', n2)
    sum2 += n2


#Определение результата по сумме очков за 5 бросков
if sum1 > sum2:
    print('Выиграл игрок: ', igrok1, "кол-во баллов: ", sum1)
elif sum1 < sum2:
    print('Выиграл игрок: ', igrok2, "кол-во баллов: ", sum2)
else:
    print('Ничья!')
