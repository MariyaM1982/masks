import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [("1234567890123456", "123456******3456"), ("1234567890", "1234567890"), ("", "")],
)
def test_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "acc_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_mask_account(acc_number: str, expected: str) -> None:
    """Функция передает строку с номером счета"""
    assert get_mask_account(acc_number) == expected
