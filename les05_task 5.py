import time

# ---- Вариант 1. Решение в "лоб"
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
start = time.perf_counter()
result = [i for i in src if src.count(i) == 1]
print(result)
print(time.perf_counter()-start)


# ----- Вариант 2. Решение с множествами - более оптимальный
start = time.perf_counter()
uniq_num = set()
tmp = set()
for num in src:
    if num not in tmp:
        uniq_num.add(num)
    else:
        uniq_num.discard(num)
    tmp.add(num)
print(uniq_num)

uniq_num_ord = [num for num in src if num in uniq_num]
print(uniq_num_ord)
print(time.perf_counter()-start)
