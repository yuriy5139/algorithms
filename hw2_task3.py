def reverse(num):
    while num > 0:
        print(num % 10, end='')
        num = num // 10


reverse(99088307653)
