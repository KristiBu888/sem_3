# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1


from random import randint

n = int(input("введите количество элементов в массиве n: "))
el_x = int(input("введите x: "))
count = 0
list_els_n = []


for i in range(n):
    list_els_n.append(randint(0, 10))
for i in list_els_n:
    if i == el_x:
        count += 1

print(list_els_n)
print(f"Число {el_x} встречается {count} раз")


# решение 2
list_1 = [1, 2, 3, 4, 5]
k = 3

count = 0
for i in list_1:
    if i == k:
        count += 1
print(list_1)
print(f"Число {k} встречается {count} раз")
