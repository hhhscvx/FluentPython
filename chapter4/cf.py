import unicodedata
import sys
from pprint import pprint


START, END = ord(' '), sys.maxunicode + 1


def find(*query_words, start=START, end=END) -> None:
    query = {w.upper() for w in query_words}
    for code in range(start, end):
        char = chr(code)
        print('code', code)
        name = unicodedata.name(char, None)
        print('name', name)
        print('query', query)
        print('name split:', name.split() if name is not None else "")
        if name and query.issubset(name.split()):
            print(f'U+{code:04X}\t{char}\t{name}')


def main(words):
    if words:
        find(*words)
    else:
        print("Please provide words to find")


if __name__ == "__main__":
    pprint(sys.argv)
    main(sys.argv)
