import asyncio
import concurrent.futures

def count_lines(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        return f"{filename} -> {len(lines)} lines"

def heavy_calculation(n):
    total = 0
    for i in range(n):
        total += i * i
    return f"Sum of squares up to {n} = {total}"

async def async_task(task_name, delay):
    print(f"Starting {task_name}...")
    await asyncio.sleep(delay)
    print(f"Finished {task_name} after {delay} seconds")
    return f"{task_name} completed"

async def run_asyncio_tasks():
    print("\n=== Asyncio: Simulated Async Tasks ===")
    tasks = [
        async_task("Task A", 1),
        async_task("Task B", 2),
        async_task("Task C", 3)
    ]
    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

async def main():
    files = ["sample1.txt", "sample2.txt", "sample3.txt"]

    print("=== Thread: File Reading ===")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(count_lines, files)

    for result in results:
        print(result)

    print("\n=== Process Pool: Heavy Calculation ===")
    numbers = [1000000, 2000000, 3000000]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(heavy_calculation, numbers)

    for result in results:
        print(result)

    await run_asyncio_tasks()

if __name__ == "__main__":
    asyncio.run(main())