# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

start_value = int(input('Enter the initial number of the progression : '))
sequence_diff = int(input('Enter the difference number of the progression : '))
members_count = int(input('Enter the count of members of the progression : '))

sequence = [start_value + sequence_diff*(i) for i in range(members_count)]

print(sequence)
