from unittest.mock import patch

import pytest

from src.external_api import get_rub_amount


def test_get_rub_amount_rub():
    tx = {"amount": 123.45, "currency": "RUB"}
    assert get_rub_amount(tx) == 123.45


@patch("external_api.requests.get")
def test_get_rub_amount_usd(mock_get):
    mock_get.return_value.json.return_value = {"rates": {"RUB": 90.0}}
    mock_get.return_value.raise_for_status = lambda: None
    tx = {"amount": 2, "currency": "USD"}
    assert get_rub_amount(tx) == 180.0


@patch("external_api.requests.get")
def test_get_rub_amount_eur(mock_get):
    mock_get.return_value.json.return_value = {"rates": {"RUB": 100.0}}
    mock_get.return_value.raise_for_status = lambda: None
    tx = {"amount": 3, "currency": "EUR"}
    assert get_rub_amount(tx) == 300.0


def test_get_rub_amount_bad_currency():
    tx = {"amount": 10, "currency": "JPY"}
    with pytest.raises(ValueError):
        get_rub_amount(tx)
