def decorate(func): ...


# 1
@decorate
def target(): ...


# 1 то же самое что:
target = decorate(target)  # очень облегчает понимание декораторов


# @deco - просто синтаксический сахар
