import asyncio
import time
from contextlib import asynccontextmanager
from typing import AsyncIterator

# async.py
# A compact collection of asyncio examples (basic, concurrency, tasks, cancellation,
# timeouts, run_in_executor, async context manager & async iterator).
# Run this file with: python async.py



async def basic_task(name: str, delay: float) -> str:
    # Simple coroutine that simulates IO with asyncio.sleep
    await asyncio.sleep(delay)
    result = f"{name} done after {delay}s"
    print(result)
    return result


async def example_basic() -> None:
    print("\n== basic await ==")
    res = await basic_task("basic", 0.5)
    print("Returned:", res)


async def example_gather() -> None:
    print("\n== concurrency with asyncio.gather ==")
    # Run multiple coroutines concurrently and collect results
    tasks = [basic_task(f"g{i}", 0.3 + i * 0.2) for i in range(3)]
    results = await asyncio.gather(*tasks)
    print("Gather results:", results)


async def example_create_task() -> None:
    print("\n== creating background tasks (create_task) ==")
    # create_task schedules a coroutine to run in the background
    t1 = asyncio.create_task(basic_task("bg1", 1.0))
    t2 = asyncio.create_task(basic_task("bg2", 0.6))
    print("Background tasks started")
    # await them later (or not)
    await t1
    await t2
    print("Background tasks finished")


async def example_timeout() -> None:
    print("\n== timeout with asyncio.wait_for ==")
    try:
        # This will raise asyncio.TimeoutError if not finished in 0.5s
        await asyncio.wait_for(basic_task("timeout", 1.0), timeout=0.5)
    except asyncio.TimeoutError:
        print("Task timed out")


async def example_cancellation() -> None:
    print("\n== cancellation ==")
    long_task = asyncio.create_task(basic_task("long", 2.0))
    await asyncio.sleep(0.3)
    print("Cancelling long task...")
    long_task.cancel()
    try:
        await long_task
    except asyncio.CancelledError:
        print("Long task was cancelled")


def blocking_work(n: int) -> int:
    # Simulate CPU-bound or blocking IO work (not async)
    print(f"blocking_work start ({n})")
    time.sleep(1)  # blocking sleep
    print(f"blocking_work end ({n})")
    return n * n


async def example_run_in_executor() -> None:
    print("\n== running blocking code in executor ==")
    loop = asyncio.get_running_loop()
    # run blocking_work in default ThreadPoolExecutor
    futures = [loop.run_in_executor(None, blocking_work, i) for i in range(3)]
    results = await asyncio.gather(*futures)
    print("Executor results:", results)


class AsyncTimer:
    # Simple async context manager that times an async block
    def __init__(self, label: str = ""):
        self.label = label
        self.start = 0.0

    async def __aenter__(self):
        self.start = time.perf_counter()
        print(f"{self.label} start")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        elapsed = time.perf_counter() - self.start
        print(f"{self.label} end: {elapsed:.3f}s")


async def example_async_context_manager() -> None:
    print("\n== async context manager ==")
    async with AsyncTimer("timed block"):
        await asyncio.sleep(0.4)


class AsyncCounter:
    # An async iterator that yields numbers with a delay
    def __init__(self, count: int, delay: float = 0.2):
        self.count = count
        self.delay = delay
        self.current = 0

    def __aiter__(self) -> AsyncIterator[int]:
        return self

    async def __anext__(self) -> int:
        if self.current >= self.count:
            raise StopAsyncIteration
        await asyncio.sleep(self.delay)
        self.current += 1
        return self.current - 1


async def example_async_iterator() -> None:
    print("\n== async iterator ==")
    async for i in AsyncCounter(4, 0.15):
        print("Got:", i)


async def main() -> None:
    await example_basic()
    await example_gather()
    await example_create_task()
    await example_timeout()
    await example_cancellation()
    await example_run_in_executor()
    await example_async_context_manager()
    await example_async_iterator()


if __name__ == "__main__":
    asyncio.run(main())