"""I6 — Buggy discount calculator (fixed version)."""
from dataclasses import dataclass


@dataclass
class LineItem:
    sku: str
    qty: int
    unit_price: float


def line_total(item: LineItem) -> float:
    if item.qty <= 0:
        raise ValueError("qty must be positive")
    return round(item.qty * item.unit_price, 2)


def apply_discount(subtotal: float, pct: float) -> float:
    if pct < 0 or pct > 100:
        raise ValueError("discount pct out of range")
    # BUG (fixed): was `subtotal - subtotal * pct` (treated pct as fraction wrongly)
    return round(subtotal * (1 - pct / 100), 2)


def cart_total(items: list[LineItem], discount_pct: float = 0.0) -> float:
    subtotal = sum(line_total(i) for i in items)
    return apply_discount(subtotal, discount_pct)
