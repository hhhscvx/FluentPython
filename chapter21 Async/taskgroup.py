import asyncio
import time


async def delay(seconds: int) -> int:
    print(f"delay({seconds=}) started", flush=True)
    await asyncio.sleep(delay=seconds)
    print(f"delay({seconds=}) finished", flush=True)
    return seconds


async def main():
    start_time = time.perf_counter()
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(delay(sec)) for sec in (1, 3, 2)]  # Создаем таски и они выполняются при выходе из tg
        print(f'after create')
    print('только вышел из tg')
    print([task.result() for task in tasks])

    print(f"elapsed time: {time.perf_counter() - start_time:.1f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
