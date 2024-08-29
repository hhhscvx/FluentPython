"""Объект создается раньше"""


class Gizmo:
    def __init__(self) -> None:
        print(f'Gizmo id: {id(self)}')


x = Gizmo()

try:
    y = Gizmo() * 10
except:
    print('TypeError')

print(dir(Gizmo)) # y не присвоена | Объект создан
