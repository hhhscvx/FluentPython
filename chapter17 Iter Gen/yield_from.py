def sub_gen():
    yield 1.1
    yield 1.2


# def gen():
#     """skuf"""
#     yield 1
#     for i in sub_gen():
#         yield i
#     yield 2

def gen():
    yield 1
    yield from sub_gen()  # vibe
    yield 2


for x in gen():
    print(x)
