import csv

import pandas as pd

""" Чтение файла transactions.csv с помощью функции csv.reader"""
with open("../data/transactions.csv") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # убираем строку с заголовком таблицы
    for row in reader:
        print(row)

""" Чтение файла transactions.csv и создание словаря с помощью функции DictReader"""
with open("../data/transactions.csv") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)

""" Чтение файла transactions.csv с помощью функции pd.read_csv"""
csv_data = pd.read_csv("../data/transactions.csv")
print(csv_data.shape)  # узнаем размер таблицы
print(csv_data.head())  # выводим информацию из первых 5 строк
print(csv_data.head(1000))

""" Чтение файла transactions.csv с помощью функции pd.read_excel"""
excel_data = pd.read_excel("../data/transactions_excel.xlsx")
print(excel_data.shape)  # узнаем размер таблицы
print(excel_data.head())  # выводим информацию из первых 5 строк
print(excel_data.head(1000))
