import json
from pathlib import Path
from typing import Any, Dict, List

def load_transactions(json_path: str) -> List[Dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.
    Если файл не найден, пустой или содержит не список — возвращает [].
    """
    path = Path(json_path)
    if not path.is_file():
        return []
    try:
        content = path.read_text(encoding="utf-8")
        if not content.strip():
            return []
        data = json.loads(content)
        if isinstance(data, list):
            return data
    except (json.JSONDecodeError, OSError):
        pass
    return []