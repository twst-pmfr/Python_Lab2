def add(a,b): #операция сложения
    return a+b
def subtract(a,b): #операция вычитания
    return a-b
def multiply(a,b): #операция умнажения
    return a*b
def divide(a,b): #операция деления
    if b==0:
        raise ZeroDivisionError('Ошибка: деление на 0') #предотвращение деления на 0
    return a/b
