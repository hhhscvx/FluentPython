import asyncio
import time


async def delay(seconds: int) -> int | None:
    print(f"delay({seconds=}) started", flush=True)
    if seconds == 3:
        raise Exception('proebali')
    await asyncio.sleep(delay=seconds)
    print(f"delay({seconds=}) finished", flush=True)
    return seconds


async def main():
    start_time = time.perf_counter()
    # await delay(1) # синхронизация (zalupa)
    # await delay(3)
    # await delay(2)
    tasks = [delay(i) for i in (1, 3, 2)]  # gather сам сделает create_task
    gather = await asyncio.as(*tasks,  # vibe
                                  return_exceptions=True)  # ошибка не прервет выполнение остальных тасок
    print('result:', gather)
    print(f"elapsed time: {time.perf_counter() - start_time:.1f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
