# 1.	Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. (готово)
# Результаты обхода сохраните в файлы json, csv и pickle.
# - Для дочерних объектов указывайте родительскую директорию. (готово)
# - Для каждого объекта укажите файл это или директория.
# - Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

# 2.	Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.


import os
import json
import csv
import pickle
import glob


path = "C:\Program Files\Speedtest"  # адрес директории

def obxodFile(path):

    print( 'В ней находятся:', os.listdir(path))

    for i in os.listdir(path):     # рекурсивно обходим все директории
        if os.path.isdir(path + '\\' + i):
            for filename in os.listdir(path):
                f = os.path.join(path, filename)

                if os.path.isfile(f):   # тут смотрим на размер файла в байтах
                    file_stats = os.stat(f)
                    print(f, ' = file. This size = ', file_stats.st_size, "byte")

                if os.path.isdir(f):    # а тут не получилось посчитать вес директории.
                    print(f, " = dir")



            print ("_" * 100)
            print('Родительская директория: ', path + '\\' + i)
            obxodFile(path + '\\' + i, )


        with open ('new_json_file','a',encoding= "utf-8") as f:     # записываем в формате json
            json.dump ((path, os.listdir(path)), f)

        with (
            open('new_csv_file.csv', 'a', newline='', encoding='utf-8')   # записываем в формате csv
            as f_write
        ):
            csv_write = csv.writer(f_write, dialect='excel', delimiter='_', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            all_data = []
            all_data.append(os.listdir(path))
            csv_write.writerows(all_data)

        with open('new_pickle_file.pickle', 'a') as f:  # записываем в pickle
            pickle.dump (os.listdir(path), f)

obxodFile(path)

if __name__ == "__main__":
    print()

