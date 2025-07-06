from typing import Dict, List

import pandas as pd


def read_transactions_from_csv(file_path: str) -> List[Dict]:
    """Функция считывает финансовые операции из CSV-файла.
    Принимает на вход в качестве аргумента путь к файлу CSV
    и возвращает список словарей с транзакциями.
    """
    df = pd.read_csv("data/transactions.csv")
    transaction_csv = df.to_dict(orient="records")
    return transaction_csv


def read_transactions_from_excel(file_path: str) -> List[Dict]:
    """Функция считывает финансовые операции из EXCEL-файла.
    Принимает на вход в качестве аргумента путь к файлу EXCEL
    и возвращает список словарей с транзакциями.
    """
    df = pd.read_excel("data/transactions_excel.xlsx")
    transaction_excel = df.to_dict(orient="records")
    return transaction_excel


if __name__ == "__main__":
    csv_transactions = read_transactions_from_csv("data/transactions.csv")
    print(csv_transactions)

    excel_transactions = read_transactions_from_excel("data/transactions_excel.xlsx")
    print(excel_transactions)
