"""Input checks for pure accounting primitives; no provider or payment access."""


def integer_minor(value: object, name: str, *, minimum: int = 0) -> int:
    # bool subclasses int in Python, but is never a monetary quantity here.
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return value


def nonblank(value: object, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} is required and must be text")
    return value
