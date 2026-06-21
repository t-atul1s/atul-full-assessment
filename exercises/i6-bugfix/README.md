# I6 — Bug Fix Exercise

## Bug

`apply_discount` treated `pct` as a raw multiplier instead of a percentage, so `10` meant `-900` instead of `10% off`.

## Reproduce (before fix)

```python
apply_discount(100, 10)  # returned -900
```

## Verify

```bash
pytest tests/ -v
```

## Verification

Re-run pytest and spot-check `cart_total` with mixed line items after applying the fix.
