import os

import requests
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")


def get_rub_amount(transaction: dict) -> float:
    """
    Принимает транзакцию и возвращает сумму в рублях (float).
    Если валюта — RUB, возвращает amount как есть.
    Для USD/EUR выполняет конвертацию через внешний API.
    """
    amount = float(transaction["amount"])
    currency = transaction.get("currency", "RUB").upper()
    if currency == "RUB":
        return amount

    if currency in ("USD", "EUR"):
        url = f"https://apilayer.com/marketplace/exchangerates_data-api={currency}&symbols=RUB"
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        rate = data["rates"]["RUB"]
        return round(amount * rate, 2)
    raise ValueError(f"Unsupported currency: {currency}")
