import re
import reprlib


RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text) -> None:
        self.text = text
        self.words: list = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self) -> int:
        return len(self.words)

    def __repr__(self) -> str:
        return f'Sentence(text={reprlib.repr(self.text)})'

    """Итератор👇"""

    def __iter__(self):
        for word in self.words:
            yield word


s = Sentence("Bebra become human asyncio web3py (huinya)")  # reprlib Sentence(text='Bebra become...b3py (huinya)')
print(s)

for penis in s * 15000:
    print(penis)
