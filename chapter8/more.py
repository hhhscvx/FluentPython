from typing import Callable


Callable[[float, float], None]  # [[params], return]


'---------------'


def tag(__name: str,  # чисто позиционные аргументы можно обозначить с __
        *content: str,
        class_: str | None = None,
        **attrs: str
        ) -> str: ...
