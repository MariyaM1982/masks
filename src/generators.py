from typing import List, Dict, Iterator


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Возвращает итератор по транзакциям, у которых валюта совпадает с переданной.
    """
    for transaction in transactions:
        if transaction.get("currency") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор, возвращающий описание каждой транзакции.
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.
    Числовые значения генерируются от 'start' до 'stop' включительно.
    """
    for num in range(start, stop + 1):
        # Преобразуем число в 16-значную строку с ведущими нулями.
        card_str = str(num).zfill(16)
        # Форматируем в виде XXXX XXXX XXXX XXXX
        formatted = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"
        yield formatted
