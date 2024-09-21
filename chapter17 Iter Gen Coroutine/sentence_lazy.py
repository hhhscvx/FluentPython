import re
import reprlib


RE_WORD = re.compile(r'\w+')


class SentenceLazy:
    def __init__(self, text) -> None:
        self.text = text

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self) -> int:
        return len(self.words)

    def __repr__(self) -> str:
        return f'Sentence(text={reprlib.repr(self.text)})'

    def __iter__(self):
        """finditer ищет именно в момент итерации (экономим при большом кол-ве yield`ов)"""
        for word in RE_WORD.finditer(self.text):
            yield word

        # Генераторное выражение (ахуеть я не знал что такое есть)
        return (match.group() for match in RE_WORD.finditer(self.text))
