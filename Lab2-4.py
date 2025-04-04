import re #модуль для работы с регулярными выражениями

# Функция для чтения файла
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# Функция для записи результатов в файл
def write_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(item + '\n')

# Регулярное выражение для поиска email-адресов
email_pattern = r'[\w.-]+@[\w-]+\.[\w.-]+'

# Регулярное выражение для поиска номеров телефонов в формате +7-XXX-XXX-XX-XX
phone_pattern = r'\+7-\d{3}-\d{3}-\d{2}-\d{2}'

# Регулярное выражение для поиска слов, начинающихся с заглавной буквы
capital_word_pattern = r'\b[A-ZА-Я][a-zа-я]*\b'

# Чтение текста из файла
text = read_file('text.txt')

# Поиск всех email-адресов
emails = re.findall(email_pattern, text)
write_to_file('emails.txt', emails)

# Поиск всех номеров телефонов
phones = re.findall(phone_pattern, text)
write_to_file('phones.txt', phones)

# Поиск всех слов, начинающихся с заглавной буквы
capital_words = re.findall(capital_word_pattern, text)
write_to_file('capital_words.txt', capital_words)
