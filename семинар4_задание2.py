N = int(input("введите количество кустов: "))
list1 = []
for i in range(1, N + 1):
    list1.append(int(input(f"введите количество ягод на кусте номер {i}: ")))
    i += 1
print(list1)

list2 = []

for j in range(0, len(list1)):
    if list1[j] == list1[-1]:
        list2.append(list1[0] + list1[j] + list1[j-1])

    elif j <= 0:
        list2.append(list1[j+1] + list1[j] + list1[-1])
        j += 1
    else:
        list2.append(list1[j-1] + list1[j] + list1[j+1])
        j += 1
print(list2)

print(f"максимальное количество ягод -> {max(list2)}")