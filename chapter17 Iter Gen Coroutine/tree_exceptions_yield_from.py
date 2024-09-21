from collections.abc import Iterator


def tree(cls: object, level: int = 0) -> Iterator[tuple[str, int]]:
    yield cls.__name__, level
    for sub_cls in cls.__subclasses__():
        yield from tree(sub_cls, level + 1)


def display(cls: object) -> None:
    for cls_name, level in tree(cls):
        print(' ' * 4 * level, cls_name)


if __name__ == "__main__":
    display(BaseException)
