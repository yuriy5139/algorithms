def calc():
    while True:
        inp = input("Ведите пример для расчета, разделяя операнды и знак операции пробелами ")
        if inp.split(' ')[1] == '0':
            break
        try:
            print(eval(inp))
        except ZeroDivisionError:
            print("Деление на 0 запрещено")

calc()