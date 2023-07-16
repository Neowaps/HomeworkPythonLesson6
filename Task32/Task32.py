# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

countElements = 8     # тут произвольное количество элементов массива
minVol = int(input("Введите минимальное значение: "))
maxVol = int(input("Введите максимальное значение: "))

array = []
for i in range(countElements):
    array.append(randint(1, 50))
index = []
for i in range(countElements):
    if array[i] <= maxVol and array[i] >= minVol:
        index.append(i)
print(array)
print(index)
