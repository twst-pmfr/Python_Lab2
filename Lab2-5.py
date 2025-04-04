#создаём список из чисел от 1 до 20
line = []
for i in range(1,20+1):
    line.append(i)
print(line)
#отбираем из списка только чётные числа
even = []
for i in line:
    if i%2==0:
        even.append(i)
print(even)
#увиличиваем каждое число на 10
for i in range(len(even)):
    even[i] += 10
print(even)
#сортируем список по убыванию
even.sort(reverse=True)
print(even)
