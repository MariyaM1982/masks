# Проект "Банковские операции"

## Описание:

Проект "Банковские операции" - Это виджет на Python для презжентации нескольих последних
успешных банковских операций клиента. 

## Установка:

1. Клонируйте репозиторий:
```
git@github.com:MariyaM1982/masks.git
```

2. Установите зависимости:
```
pip install -r requirements.txt
```
## Иcпользование

1. Функция маскировки номера банковской карты
get_mask_card_number

2. Функция маскировки номера банковского счета 
get_mask_account

3. функция обработки информации о картах и о счетах 
mask_account_card

4. Функция обработки формата даты get_date
   
5. функция sort_by_date

6. Функции read_transactions_from_csv для считывания информации из фала CSV и функция read_transactions_from_excel для считывания информации из фала EXCEL

## Тестирование

В папке \tests тест-кейсы (test_masks.py, test_widget.py, test_processing.py, test_generators.py, test_decorators.py, test_external_api.py, test_utils.py, test_transaction_reader.py) для тестирования модулей: masks, widget, processing, generators, utils, decorators, external_api, transaction_reader.

