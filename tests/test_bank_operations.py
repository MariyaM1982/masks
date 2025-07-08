import unittest

import pytest

from src.bank_operations import (filter_by_status, filter_rub_transactions,
                                 process_bank_operations, process_bank_search,
                                 sort_by_date)


@pytest.fixture
def sample_data():
    return [
        {"description": "Открытие вклада", "status": "EXECUTED"},
        {"description": "Перевод с карты на карту", "status": "EXECUTED"},
        {"description": "Перевод организации", "status": "CANCELED"},
        {"description": "Перевод со счета на счет", "status": "EXECUTED"},
    ]


def test_process_bank_operations(sample_data):
    categories = ["перевод", "открытие вклада"]
    result = process_bank_operations(sample_data, categories)
    assert result == {"перевод": 3, "открытие вклада": 1}


class TestBankOperations(unittest.TestCase):

    def setUp(self):
        self.sample_data = [
            {
                "date": "08.12.2019",
                "description": "Открытие вклада",
                "status": "EXECUTED",
                "amount": "40542 руб.",
                "to": "Счет **4321",
            },
            {
                "date": "12.11.2019",
                "description": "Перевод с карты на карту",
                "status": "EXECUTED",
                "amount": "130 USD",
                "from": "MasterCard 7771",
                "to": "Visa Platinum 1293",
            },
            {
                "date": "18.07.2018",
                "description": "Перевод организации",
                "status": "CANCELED",
                "amount": "8390 руб.",
                "from": "Visa Platinum 7492",
                "to": "Счет **0034",
            },
        ]

    def test_process_bank_search(self):
        result = process_bank_search(self.sample_data, "перевод")
        self.assertEqual(len(result), 2)

    def test_filter_by_status(self):
        result = filter_by_status(self.sample_data, "EXECUTED")
        self.assertEqual(len(result), 2)

    def test_sort_by_date(self):
        result = sort_by_date(self.sample_data)
        self.assertEqual(result[0]["date"], "18.07.2018")

    def test_filter_rub_transactions(self):
        result = filter_rub_transactions(self.sample_data)
        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()
