import pytest

from app.cart import LineItem, apply_discount, cart_total, line_total


def test_line_total():
    assert line_total(LineItem("A", 3, 10.0)) == 30.0


def test_ten_percent_discount():
    items = [LineItem("A", 2, 50.0)]  # subtotal 100
    assert cart_total(items, discount_pct=10) == 90.0


def test_no_discount():
    items = [LineItem("B", 1, 25.5)]
    assert cart_total(items) == 25.5


def test_apply_discount_bounds():
    with pytest.raises(ValueError):
        apply_discount(100, 150)
