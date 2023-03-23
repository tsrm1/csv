# https://docs.python.org/3.10/library/csv.html
import csv  # для работы с csv-файлами
import sys   # для работы с ошибками


data_file = 'data.csv'
headers = ['user_name', 'user_address', 'birth_day', 'sex']
users_data = [
            {'user_name': 'Роман', 'user_address': 'address1', 'birth_day': '1945-05-09', 'sex': 'man'},
            {'user_name': 'Анна',  'birth_day': '1960-09-05', 'sex': 'woman'},
            {'user_name': 'Елена', 'user_address': 'address3', 'sex': 'woman'},
            {'user_name': 'Катерина', 'user_address': 'address4', 'birth_day': '1991-08-24'},
            {'user_name': 'Валерия'},
            {'user_name': 'София', 'sex': 'woman'}
]

# записывает в файл заголовки столбцов и данные (в один заход)

with open(data_file, 'w', encoding='cp1251', newline='') as file:
    # w - write new file
    # cp1251 - russian encoding for Windows
    # utf-8 = default,  russian encoding for NIX (Linux, UNIX, MacOS)
    writer = csv.DictWriter(file, fieldnames=headers, delimiter=';')
    writer.writeheader()
    writer.writerows(users_data)              # writerows() - запись сразу нескольких строк


#
#
# # записываем в файл данные, сразу в один заход
# with open(data_file, 'a', encoding='cp1251', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#
#
#
# # записываем в файл данные, построчно
# for user in users_data:
#     with open(data_file, 'a', encoding='cp1251', newline='') as file:
#         # a - append to file
#         # cp1251 - russian encoding for Windows
#         # utf-8 = default,  russian encoding for NIX (Linux, UNIX, MacOS)
#         writer = csv.writer(file, delimiter=';')
#         writer.writerow(user)                 # writerow() - запись одной строки


# читаем данные из файла, как словарь
with open(data_file, newline='') as file:
    reader = csv.DictReader(file, delimiter=';')            # DictReader() - чтение файла как словарь
    try:
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(data_file, reader.line_num, e))

print()
# читаем данные из файла, как список
with open(data_file, newline='') as file:
    reader = csv.reader(file, delimiter=';')                # reader() - чтение файла как список
    try:
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(data_file, reader.line_num, e))