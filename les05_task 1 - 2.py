#  ------------------ Задание №1


def odd_nums(n):
    for i in range(1, n + 1, 2):
        yield i


n = int(input('Введите число n: '))
odd_to_n = odd_nums(n)
# print(next(odd_to_15)) - не через некст
print("Задача №1")
for i in odd_to_n:
    print(i)


# ----------------- Задание №2

print("Задача №2")
odd_to_n = (n for n in range(1, n + 1, 2))
for i in odd_to_n:
    print(i)
