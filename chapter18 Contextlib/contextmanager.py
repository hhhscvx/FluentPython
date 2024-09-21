from contextlib import contextmanager
import sys


@contextmanager
def looking_glass():
    """
        То, что до yield - функционал во то время, когда КМ открыт
        то, что после yield - после закрытие контекстного менеджера
        То, что yield`им - будет присвоено в YILD: `with looking_glass() as YILD`
    """
    original_write = sys.stdout.write

    def reverse_write(text) -> None:
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = original_write
