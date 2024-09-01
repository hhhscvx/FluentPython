registry = set()

"""Передача параметров в декоратор"""


def register(active=True):
    def decorate(func):
        print('running register'
              f'(active={active}) -> decorate({func.__name__})')
        if active:
            registry.add(func.__name__)
        else:
            registry.discard(func.__name__)

    return decorate


@register(active=False)
def f1():
    print('running f1()')


@register()
def f2():
    print('running f2()')


def f3():
    print('running f3()')


print(registry)
