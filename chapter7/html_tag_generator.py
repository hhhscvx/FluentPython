"""
    Ашалеть все что слева от '/' - это аргументы,
    которые можно передать только позиционно (не key-value)
"""


def tag(name, /, *content, class_=None, **attrs) -> str:
    if class_ is not None:
        attrs['class'] = class_

    attrs_all = [f' {attr}="{value}"' for attr, value in attrs.items()]
    attrs = ''.join(attrs_all)
    if content:
        elements = (f'<{name}{attrs}>{c}</{name}>' for c in content)
        return '\n'.join(elements)
    return f'<{name}{attrs} />'


print(tag('br'))

print(tag('div', "Hello", class_="container", **{'data-goods-id': 1}))
