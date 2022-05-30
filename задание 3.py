# метод sum(a,b) принимает 2 числа и возвращает их сумму.
# Написать декоратор, который возвращает ошибку
# если переданы нечисловые параметры(например строка)
#
# примерно такое:

def summa_check_int(fn):
    def summa_fun(x, y):
        try:
            fn(x, y)
        except TypeError:
            print(f'{str(fn.__name__)}{x , y} - ошибка!')
        else:
            print(f'{str(fn.__name__)}{x, y} - {fn(x, y)}')
    return summa_fun


@ summa_check_int
def summa(a,  b):
    return a+b


summa(2, 128)
summa(6, '1488')






