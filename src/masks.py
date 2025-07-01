import logging

# Настройка логирования для модуля masks
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_handler.setLevel(logging.DEBUG)

# Форматирование логов
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты в формате - 7000792289606361,
    и возвращает ее маску 7000 79** **** 6361."""

    logger.debug(f"Получение маски для номера карты: {card_number}")

    logger.info("Маска карты успешно создана")

    return (
        card_number[:4] + " " + card_number[4:6] + "**" + " **** " + card_number[12:16]
    )


print(get_mask_card_number(str()))


def get_mask_account(bank_account_number: str) -> str:
    """Принимает на вход номер счета в формате- 73654108430135874305 и
    возвращает его маску **4305."""

    logger.debug(f"Получение маски для номера счета: {bank_account_number}")

    logger.info("Маска счета успешно создана")

    return "**" + bank_account_number[-4:]


print(get_mask_account(str()))
