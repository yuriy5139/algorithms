num = int(input("Введите количество элементов ряда "))

res, div, mul = 0, 1, 1

for i in range(num):
    print(i, 1 / div * mul)
    res = res + 1 / div * mul
    div = div * 2
    mul = mul * (-1)

print("Результат: ", res)
