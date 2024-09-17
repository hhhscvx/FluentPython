from typing import TypeVar, Generic


class Refuse:
    """Отходы."""


class Biodegradable(Refuse):
    """Разлагающиеся отходы."""


class Compostable(Biodegradable):
    """Компостируемые отходы."""


T_contra = TypeVar('T_contra', contravariant=True)  # <2>


class TrashCan(Generic[T_contra]):  # <3>
    def put(self, refuse: T_contra) -> None:
        """Store trash until dumped."""


def deploy(trash_can: TrashCan[Biodegradable]):
    """Deploy a trash can for biodegradable refuse."""


bio_can: TrashCan[Biodegradable] = TrashCan()
deploy(bio_can)

trash_can: TrashCan[Refuse] = TrashCan()
deploy(trash_can)


"""
    Контрвариантность: подходят под deploy Biodegradable, и его родительские классы, все кто ниже сосут
    т.е. полная противоположность инвариантности (логично)
"""


compost_can: TrashCan[Compostable] = TrashCan()
deploy(compost_can)
# mypy: Argument 1 to "deploy" has
# incompatible type "TrashCan[Compostable]"
# expected "TrashCan[Biodegradable]"
# end::DEPLOY_NOT_VALID[]
