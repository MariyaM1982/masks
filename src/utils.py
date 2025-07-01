import json
import logging
from pathlib import Path
from typing import Any, Dict, List

# Настройка логирования
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)  # Уровень логирования не ниже DEBUG

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_handler.setLevel(logging.DEBUG)

# Создание и установка форматера
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def load_transactions(json_path: str) -> List[Dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.
    Если файл не найден, пустой или содержит не список — возвращает [].
    """
    path = Path(json_path)
    if not path.is_file():
        logger.error(f"Файл не найден: {json_path}")
        return []
    try:
        content = path.read_text(encoding="utf-8")
        if not content.strip():
            return []
        data = json.loads(content)
        if isinstance(data, list):
            logger.info(f"Транзакции успешно загружены из файла: {json_path}")
            return data
    except (json.JSONDecodeError, OSError):
        logger.error(f"Ошибка при декодировании JSON из файла {json_path}")
        pass
    return []
