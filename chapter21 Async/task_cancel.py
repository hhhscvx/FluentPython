import asyncio
import time


async def delay(seconds: int) -> None:
    print(f"delay({seconds=}) started", flush=True)
    await asyncio.sleep(delay=seconds)
    print(f"delay({seconds=}) finished", flush=True)


async def main():
    start_time = time.perf_counter()
    tasks = (
        asyncio.create_task(delay(1), name="delay 1 sec"),
        asyncio.create_task(delay(3), name="delay 3 sec"),
        asyncio.create_task(delay(20000), name="delay 20000 sec"),
    )
    for task in tasks:
        if task.get_name() == "delay 20000 sec":
            task.cancel()
        else:
            await task
    print(f"elapsed time: {time.perf_counter() - start_time:.1f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
