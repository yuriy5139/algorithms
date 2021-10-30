def odd_even(num):
    odd, even = 0, 0
    while num > 0:
        if num % 10 == 0:
            print("найден ноль")
        elif num % 10 % 2 == 0:
            print("найдено четное число", num % 10)
            even += 1
        else:
            print("найдено нечетное число", num % 10)
            odd += 1
        num = num // 10

    print(f'Четных {even}, нечетных {odd}')


odd_even(99088307653)
