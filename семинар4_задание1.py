n = int(input("введите колличество элементов первого множества: "))
m = int(input("введите колличество элементов второго множества: "))
list1 = []
list2 = []
for i in range(0, n):
    list1.append(int(input()))
    i += 1
print(list1)

for j in range(0, m):
    list2.append(int(input()))
    i += 1
print(list2)

# list1 = [13,15,6,4,13, 1000]
# list2 = [14,15,4,325,1]

list3 = list1 + list2

print(list3)
print(sorted(set(list3)))
