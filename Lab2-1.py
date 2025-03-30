data = [] #создаём пустой массив
with open('data.txt') as f: #открываем файл
    for line in f: #для кадой строки в файле
        data.extend([float(x) for x in line.split()]) #добавляем в массив все числа в файле
print(data)
su = sum(data)
print(su)
sr = su/len(data) #сумму делим на количество слагаемых
print(sr)
ma=max(data) #ищем максимум
print(ma)
mi=min(data) #ищем минимум
print(mi)
f.close()

file = open('result.txt','w') #открываем новый файл и записываем результаты
file.write('Сумма: ' + str(su) + '\n')
file.write('Среднее: ' + str(sr) + '\n')
file.write('Максимум: ' + str(ma) + '\n')
file.write('Минимум: ' + str(mi) + '\n')
file.close()
