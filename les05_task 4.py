src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# Необходимо вывести те его элементы, значения которых больше предыдущего, например:
result = [num[1] for num in enumerate(src[1:]) if src[num[0]] < num[1]]
print(result)