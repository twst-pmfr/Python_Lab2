import re
from datetime import datetime

# Чтение текста из файла text.txt
with open('text(6).txt', 'r') as file:
    text = file.read()

# Поиск всех дат формата DD.MM.YYYY с помощью регулярного выражения
date_pattern = r'\d{2}\.\d{2}\.\d{4}'
dates_dd_mm_yyyy = re.findall(date_pattern, text)

# Преобразование дат в формат YYYY-MM-DD
formatted_dates = []
for date_str in dates_dd_mm_yyyy:
    try:
        # Парсинг строки даты в объект datetime
        dt_obj = datetime.strptime(date_str, '%d.%m.%Y')
        # Форматирование даты в нужный формат
        formatted_date = dt_obj.strftime('%Y-%m-%d')
        formatted_dates.append(formatted_date)
    except ValueError:
        print(f'Ошибка при парсинге даты: {date_str}')

# Запись преобразованных дат в файл dates.txt
with open('dates.txt', 'w') as file:
    for date in formatted_dates:
        file.write(date + '\n')

# Сортировка дат по возрастанию с использованием лямбды
sorted_dates = sorted(formatted_dates, key=lambda x: datetime.strptime(x, '%Y-%m-%d'))

# Вывод отсортированных дат
for date in sorted_dates:
    print(date)
