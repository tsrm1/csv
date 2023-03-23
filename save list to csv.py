# https://docs.python.org/3.10/library/csv.html
import csv  # для работы с csv-файлами
import sys   # для работы с ошибками


data_file = 'data.csv'
headers = ['user_name', 'user_address', 'birth_day', 'sex']

# записывает в файл заголовки столбцов

with open(data_file, 'w', encoding='cp1251', newline='') as file:
    # w - write new file
    # cp1251 - russian encoding for Windows
    # utf-8 = default,  russian encoding for NIX (Linux, UNIX, MacOS)
    writer = csv.writer(file, delimiter=';')
    writer.writerow(headers)


users_data = [
    ['Роман', 'address1', '1945-05-09', 'man'],
    ['Анна', 'address2', '1960-09-05', 'woman'],
    ['Елена', 'address3', '1976-03-03', 'woman'],
    ['Катерина', 'address4', '1991-08-24', 'woman'],
    ['Валерия', 'address5', '2009-09-10', 'woman'],
    ['София', 'address6', '2012-03-18', 'woman'],
]


# записываем в файл данные, сразу в один заход
with open(data_file, 'a', encoding='cp1251', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(users_data)              # writerows() - запись сразу нескольких строк


# записываем в файл данные, построчно
for user in users_data:
    with open(data_file, 'a', encoding='cp1251', newline='') as file:
        # a - append to file
        # cp1251 - russian encoding for Windows
        # utf-8 = default,  russian encoding for NIX (Linux, UNIX, MacOS)
        writer = csv.writer(file, delimiter=';')
        writer.writerow(user)                 # writerow() - запись одной строки


# читаем данные из файла
with open(data_file, newline='') as file:
    reader = csv.reader(file, delimiter=';')
    try:
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(data_file, reader.line_num, e))