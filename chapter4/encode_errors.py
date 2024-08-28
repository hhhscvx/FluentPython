import locale


s = "cãfè"

"""Обработка UnicodeDecodeError (в cp437 нет ã)"""
print(s.encode('cp437', errors="ignore"))  # b'cf\x8a'
print(s.encode('cp437', errors="replace"))  # b'c?f\x8a'
print(s.encode('cp437', errors="xmlcharrefreplace"))  # b'c&#227;f\x8a'

print('---------')
"""
    Если возникает SyntaxError, можно попробовать в первую
    строку файла написать комментарий `# coding: cp1252`
"""

print('\N{INFINITY}')
print('\N{CIRCLED NUMBER FORTY TWO}')

"""
    всегда нужно указывать конкретный кодек,
    потому что на разных OS разные preferredencoding
"""
print(locale.getpreferredencoding())
