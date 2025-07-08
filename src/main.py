import csv
import json

import pandas as pd

from src.bank_operations import (filter_by_status, filter_rub_transactions,
                                 print_transactions, process_bank_search,
                                 sort_by_date)


def load_json(file_path):
    with open("data/operations.json", "r", encoding="utf-8") as file:
        return json.load(file)


def load_csv(file_path):
    with open("data/transactions.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


def load_xlsx(file_path):
    df = pd.read_excel("data/transactions_excel.xlsx")
    return df.to_dict(orient="records")


def main():
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\nВыберите необходимый пункт меню:"
    )
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Ваш выбор: ")
    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        data = load_json("data/operations.json")
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        data = load_csv("data/transactions.csv")
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        data = load_xlsx("data/transactions_excel.xlsx")
    else:
        print("Некорректный выбор.")
        return

    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = input(
            f"\nВведите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтрации статусы: {', '.join(valid_statuses)}\n"
        ).upper()
        if status not in valid_statuses:
            print(f'Статус операции "{status}" недоступен.')
        else:
            break

    data = filter_by_status(data, status)
    print(f'Операции отфильтрованы по статусу "{status}"')

    if input("\nОтсортировать операции по дате? Да/Нет\n").lower() == "да":
        order = input("Отсортировать по возрастанию или по убыванию?\n").lower()
        data = sort_by_date(data, reverse=(order == "по убыванию"))

    if input("\nВыводить только рублевые транзакции? Да/Нет\n").lower() == "да":
        data = filter_rub_transactions(data)

    if (
        input(
            "\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n"
        ).lower()
        == "да"
    ):
        search = input("Введите слово для поиска в описании: ")
        data = process_bank_search(data, search)

    print("\nРаспечатываю итоговый список транзакций...\n")
    print_transactions(data)


if __name__ == "__main__":
    main()
