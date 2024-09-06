

class Pixel:
    """
        Задавать классу можно только атрибуты, перечисленные в slots.
        Если ты адекват и не будешь определять не определенное - надо юзать slots
    """
    __slots__ = ('x', 'y')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'


p = Pixel()
p.x = 10
p.y = 20
p.bebra = 'red'  # AttributeError

print(p)
