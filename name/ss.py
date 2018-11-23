list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 3, 5, 7, 9]
for i in range(0, len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] == list1[j]:
            list1.remove(list1[i])

print(list1)
