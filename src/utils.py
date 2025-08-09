from decimal import Decimal, InvalidOperation

def validate_symbol(sym: str) -> str:
    if not sym or not sym.isalnum():
        raise ValueError("Symbol must be alphanumeric like BTCUSDT")
    return sym.upper()

def validate_positive_number(value: str, name="value") -> Decimal:
    try:
        v = Decimal(value)
    except InvalidOperation:
        raise ValueError(f"{name} must be a number")
    if v <= 0:
        raise ValueError(f"{name} must be > 0")
    return v