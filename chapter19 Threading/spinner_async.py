import itertools
import asyncio
from asyncio.exceptions import CancelledError


async def spin(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        try:
            await asyncio.sleep(.1)
        except CancelledError:
            break
        blanks = ' ' * len(status)
        print(f'\r{blanks}\r', end='')


async def slow() -> int:
    await asyncio.sleep(3)
    return 42


async def supervisor() -> int:
    spinner = asyncio.create_task(spin(msg='threading!'))
    print(f'spinner object: {spinner}')
    result = await slow()
    spinner.cancel()
    return result


def main() -> None:
    result = asyncio.run(supervisor())
    print(f'Answer: {result}')


if __name__ == "__main__":
    main()
