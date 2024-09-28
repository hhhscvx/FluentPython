import asyncio
import time


async def delay(seconds: int) -> None:
    print(f"delay({seconds=}) started", flush=True)
    await asyncio.sleep(delay=seconds)
    print(f"delay({seconds=}) finished", flush=True)


async def main():
    start_time = time.perf_counter()
    tasks = [asyncio.create_task(coro=delay(sec), name=f"delay {sec} sec") for sec in (1, 3, 2)]
    done, pending = await asyncio.wait(tasks, timeout=2.1) # самый продвинутый способ | vibe
    print('done:', [task.get_name() for task in done])
    print('pending:', [task.get_name() for task in pending])

    print(f"elapsed time: {time.perf_counter() - start_time:.1f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
