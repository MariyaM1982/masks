import csv
import os

import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")
CSV_PATH = os.path.join(DATA_DIR, "transactions.csv")
XLSX_PATH = os.path.join(DATA_DIR, "transactions_excel.xlsx")


def test_csv_reader_rows_count():
    """Тест на чтение CSV с помощью csv.reader и подсчет строк"""
    with open(CSV_PATH, newline="", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # пропускаем заголовок
        rows = list(reader)
    assert len(rows) > 0
    # Проверяем, что каждая строка - список строковой длины равной заголовку
    for row in rows:
        assert isinstance(row, list)
        assert len(row) == len(header)


def test_csv_dictreader_content():
    """Тест на чтение CSV с помощью csv.DictReader"""
    with open(CSV_PATH, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)
    assert len(rows) > 0
    # Проверяем, что каждая строка — словарь с ключами заголовка
    for row in rows:
        assert isinstance(row, dict)
        assert set(row.keys()) == set(reader.fieldnames)


def test_pandas_read_csv_shape_and_head():
    """Тест чтения csv через pandas и проверка формы и первых строк"""
    df = pd.read_csv(CSV_PATH)
    assert df.shape[0] > 0 and df.shape[1] > 0
    head = df.head()
    assert isinstance(head, pd.DataFrame)
    assert len(head) <= 5
    head_1000 = df.head(1000)
    assert isinstance(head_1000, pd.DataFrame)
    assert len(head_1000) <= 1000


def test_pandas_read_excel_shape_and_head():
    """Тест чтения excel через pandas с проверкой формы и первых строк"""
    df = pd.read_excel(XLSX_PATH)
    assert df.shape[0] > 0 and df.shape[1] > 0
    head = df.head()
    assert isinstance(head, pd.DataFrame)
    assert len(head) <= 5
    head_1000 = df.head(1000)
    assert isinstance(head_1000, pd.DataFrame)
    assert len(head_1000) <= 1000
