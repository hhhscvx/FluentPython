def deco(func):
    print('parasha?')  # ашалеть этот прикол всегда выполняется

    def inner():
        print('running inner()')
    return inner  # func даже нигде не отрабатывает


@deco
def target():
    print('running target()')


# target()
