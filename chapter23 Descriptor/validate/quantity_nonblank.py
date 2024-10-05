from validate_abc import Validate


class Quantity(Validate):
    """число, большее нуля"""

    def validate(self, name: str, value: int) -> int | None:
        if value <= 0:
            raise ValueError(f'{name} must be > 0')
        return value


class NonBlank(Validate):
    """Не пустая строка"""

    def validate(self, name: str, value: str) -> str | None:
        value = value.strip()
        if not value:
            raise ValueError(f'{name} can`t be blank')
