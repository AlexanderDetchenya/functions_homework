# метод sum(a,b) принимает 2 числа и возвращает их сумму.
# Написать декоратор, который возвращает ошибку
# если переданы нечисловые параметры(например строка)
#
# примерно такое:

def summa():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    sum = a + b
    return sum


def summa_decore(summa):
    def decore():
        try:
            summa()
        except ValueError:
            print('Ошибка')




summa_decore(summa)
print(summa_decore(summa))




