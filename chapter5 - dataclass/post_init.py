from dataclasses import dataclass, field
from typing import ClassVar


@dataclass(slots=True)
class ClubMember:
    name: str
    guests: list = field(default_factory=list)  # list будет у каждого экземпляра свойШ
    athlete: bool = field(default=False, repr=False)


class HackerClubMember(ClubMember):
    # ClassVar -> не генерируется поле для экземпляра
    all_handles: ClassVar[set[str]] = set()
    handle: str = ''

    def __post_init__(self) -> None:
        cls = self.__class__
        if self.handle == '':
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f'handle {self.handle!r} already exists'
            raise ValueError(msg)

        cls.all_handles.add(self.handle)
