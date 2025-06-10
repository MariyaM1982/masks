from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """Функция, которая маскирует номер счета или карты"""
    text_result = ""
    digit_result = ""
    digit_count = 0
    for el in type_and_number:
        if el.isalpha():
            text_result += el
        elif el.isdigit():
            digit_result += el
            digit_count += 1
    if digit_count > 16:
        return f"{text_result} {get_mask_account(digit_result)}"
    else:
        return f"{text_result} {get_mask_card_number(digit_result)}"


print(mask_account_card("Master Card 32145698741236980213"))


def get_date(date_of_operation: str) -> str:
    """Функция, которая возвращает строку с датой в формате ДД.ММ.ГГГГ"""

    return (
        date_of_operation[8:10]
        + "."
        + date_of_operation[5:7]
        + "."
        + date_of_operation[0:4]
    )


print(get_date("2024-03-11Т02:26:18.671407"))
