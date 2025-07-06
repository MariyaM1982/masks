import json
import os
import tempfile


from src.utils import load_transactions


def test_load_transactions_ok():
    d = [{"a": 1}, {"b": 2}]
    with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as f:
        json.dump(d, f)
        fname = f.name
    result = load_transactions(fname)
    os.remove(fname)
    assert result == d


def test_load_transactions_empty():
    with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as f:
        fname = f.name
    result = load_transactions(fname)
    os.remove(fname)
    assert result == []


def test_load_transactions_not_found():
    assert load_transactions("not_exist.json") == []


def test_load_transactions_not_list():
    with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as f:
        f.write('{"a": 1}')
        fname = f.name
    result = load_transactions(fname)
    os.remove(fname)
    assert result == []
