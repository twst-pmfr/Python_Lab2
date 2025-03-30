import math_operations #импортируем модуль с операциями
print(math_operations.add(2,3)) #выполняем сложение через модуль
print(math_operations.subtract(45,9)) #выполняем вычитание через модуль
print(math_operations.multiply(23,6)) #выполняем умножение через модуль
try:
    print(math_operations.divide(9,3)) #выполняем деление через модуль
except ZeroDivisionError as e: #предотвращение ошибки
    print(e)
