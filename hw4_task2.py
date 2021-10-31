import cProfile


# Реализация 1 - Решето Эратосфена
def sieve(n):
    # создаем список, из которого будем "вычеркивать" составные числа
    lst = [i for i in range(0, n + 1)]

    # вычеркиваем, заменяя на 0, числа, являющиеся произведением
    p = 2
    while p < n:
        i = 2
        while i * p <= n:
            lst[i * p] = 0
            i += 1
        for num in lst[p:]:
            if num > p:
                p = num
                break
        if max(lst) == p:
            break
    return [item for item in lst if item > 0][1:]


# Реализация 2: перебор с остановкой

def simple_num(n):
    res = []
    for num in range(0, n):
        marker = True
        for i in range(2, num):
            if num % i == 0:
                marker = False
                break
        if marker: res.append(num)
    return res[2:]

# Определим, сколько примерно простых чисел есть в диапазоне до 100К
# for i in [100, 500, 1000, 5000, 10000, 50000, 100000]:
#     print(i, len(sieve(i)))
#Получим следующий результат:
"""
100 25
500 95
1000 168
5000 669
10000 1229
50000 5133
100000 9592
"""
#То есть, при приближении к 100К получаем, что простых чисел в этом диапазоне чуть меньше, чем одна десятая
#Соответственно, пытаясь найти n-ое простое число, нужно рассматривать диапазон, десятикратно превышающий это число,
#если речь идет об n в пределах 10000. Чтобы наверняка, будем рассматривать двадцатикратный диапазон.

#Определение n-ого простого числа на основе Решета Эратосфена
def sieve_solution(n):
    res = sieve(n*20)
    return(res[n-1])

#Определение n-ого простого числа на основе алгоритма с перебором
def simple_solution(n):
    res = simple_num(n*20)
    return(res[n-1])

#Профилируем
cProfile.run('sieve_solution(3000)')
"""
Результат:
6063 function calls in 3.983 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.983    3.983 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 hw4_task2.py:22(<listcomp>)
        1    0.556    0.556    3.983    3.983 hw4_task2.py:5(sieve)
        1    0.000    0.000    3.983    3.983 hw4_task2.py:56(sieve_solution)
        1    0.002    0.002    0.002    0.002 hw4_task2.py:7(<listcomp>)
        1    0.000    0.000    3.983    3.983 {built-in method builtins.exec}
     6056    3.424    0.001    3.424    0.001 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

cProfile.run('simple_solution(3000)')
"""
Результат:
 6064 function calls in 6.548 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    6.548    6.548 <string>:1(<module>)
        1    6.548    6.548    6.548    6.548 hw4_task2.py:27(simple_num)
        1    0.000    0.000    6.548    6.548 hw4_task2.py:61(simple_solution)
        1    0.000    0.000    6.548    6.548 {built-in method builtins.exec}
     6059    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

#Алгоритм на основе Решета Эратосфена быстрее в 1.6 раза.