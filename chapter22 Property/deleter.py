class BlackSwordman:

    pisya = 4

    def __init__(self) -> None:
        self.phrases = [
            ('рука', 'RAGEEEEEE'),
            ('глаз', 'GRIFITHHHHHHHHHHHHHHHHHH')
        ]

    @property
    def member(self) -> str:
        return self.phrases[0][0]

    @member.deleter
    def member(self) -> None:
        member, text = self.phrases.pop(0)
        print(f'ЧЕРНЫЙ МЕЧНИК (утрачен(а) {member}) -- {text}')

    def __getattr__(self, name):
        """Этот метод вызывается тогда, когда попытка найти атрибут завершается неудачно"""
        print(f'Attr not found: {name}')


guts = BlackSwordman()

print(guts.member)

del guts.member
del guts.member
