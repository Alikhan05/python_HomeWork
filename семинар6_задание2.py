# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def list_index(list1):
    list_of_index = []
    min_num = int(input("введите минимальное значение диапозона -> "))
    max_num = int(input("введите максимальное значение диапозона -> "))
    for i in range(len(list1)):
        if min_num <= list1[i] <= max_num:
            list_of_index.append(i)
    return list_of_index

list_1 = [21, -3, 111, 44, 14 , 0 , 1 , 5]
print(list_index(list_1))
        