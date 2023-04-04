# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randrange


max_limit = int(input("Enter the max limit value (non negative) : "))
min_limit = int(input("Enter the min limit value (non negative) : "))

random_array = [randrange(0, max_limit) for i in range(max_limit * 2)]
print(random_array)

indexes_list = dict()

for i in range(len(random_array)):
    if min_limit <= random_array[i] <= max_limit:
        indexes_list[i] = random_array[i]


print(indexes_list)

