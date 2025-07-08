import re
from collections import Counter
from datetime import datetime


# Функция для поиска транзакций по тексту в описании
def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция реализует поиск операций, содержащих заданную строку в описании.
    Принимает на вход в качестве аргументов список операций и строку для поиска
    и возвращает отфильтрованный список операций
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [item for item in data if pattern.search(item.get("description", ""))]


# Функция для подсчета операций по категориям
def process_bank_operations(data: list[dict], categories: list[str]) -> dict[str, int]:
    """
    Функция реализует подсчет количества операций по категориям.
    Принимает на вход в качестве аргументов список операций и список категорий
    и возвращает словарь с количеством операций по категориям
    """
    descriptions = [item.get("description", "").lower() for item in data]
    counts = Counter()
    for category in categories:
        counts[category] = sum(1 for desc in descriptions if category.lower() in desc)
    return dict(counts)


# Фильтрация по статусу
def filter_by_status(data: list[dict], status: str) -> list[dict]:
    return [item for item in data if item.get("status", "").upper() == status.upper()]


# Сортировка по дате
def sort_by_date(data: list[dict], reverse=False) -> list[dict]:
    return sorted(
        data, key=lambda x: datetime.strptime(x["date"], "%d.%m.%Y"), reverse=reverse
    )


# Фильтрация по валюте (рублевые транзакции)
def filter_rub_transactions(data: list[dict]) -> list[dict]:
    return [item for item in data if "руб" in item.get("amount", "")]


# Красивый вывод транзакций
def print_transactions(data: list[dict]):
    if not data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(data)}\n")
    for item in data:
        print(f"{item['date']} {item['description']}")
        if "from" in item:
            print(f"{item['from']} -> {item['to']}")
        else:
            print(f"{item['to']}")
        print(f"Сумма: {item['amount']}\n")
