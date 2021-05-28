from itertools import zip_longest
from time import perf_counter

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Елена', 'Василий'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

# ----- 1. Вариант с zip_longest - быстрее второго работает
start = perf_counter()
tutor_klass_tuple = (i for i in zip_longest(tutors, klasses, fillvalue=None))
print(type(tutor_klass_tuple))
for i in tutor_klass_tuple:
    print(i)
print(perf_counter()-start)


# ----- 2. Вариант с обычным ZIP, но с 2 генераторами
start = perf_counter()
tutors_gen, klasses_gen = (i for i in tutors), (i for i in klasses)
for i in zip(tutors_gen, klasses_gen):
    print(i)
for i in tutors_gen:
    print((i, None))
print(perf_counter()-start)
