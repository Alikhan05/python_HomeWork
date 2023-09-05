# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def progressia(num, num_diference, amount):
    list1 = [num]
    for i in range(amount):
        num = num + num_diference
        list1.append(num)
    return list1

print(progressia(7,2,5))
    