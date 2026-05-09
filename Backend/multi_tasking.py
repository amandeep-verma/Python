"""
==============================================================================
PYTHON CONCURRENCY REFERENCE: asyncio, threading, multiprocessing
==============================================================================

QUICK DECISION GUIDE:
┌──────────────────────┬────────────────────────────────────────────────────┐
│ Use asyncio          │ Many I/O tasks: API calls, DB queries, file reads  │
│ Use threading        │ I/O tasks that don't support async (legacy libs)   │
│ Use multiprocessing  │ CPU-heavy work: image processing, number crunching │
└──────────────────────┴────────────────────────────────────────────────────┘

THE GIL — Why this distinction matters:
    CPython has a Global Interpreter Lock (GIL): a mutex that allows only
    ONE thread to execute Python bytecode at a time, even on multi-core CPUs.

    This means:
    - threading   → threads take TURNS, never truly parallel (GIL blocks it)
    - asyncio     → single thread, manually switches between tasks (no GIL issue)
    - multiprocessing → spawns separate processes, each with its OWN GIL → truly parallel

    GIL is NOT a problem for I/O work because:
        While a thread waits for a network response, it RELEASES the GIL.
        Another thread can then run. So threading still helps for I/O.

    GIL IS a problem for CPU work because:
        Threads compete for the GIL constantly. You get no speedup on multiple cores.
        Use multiprocessing to bypass it entirely.

    Analogy:
        GIL = one microphone in a meeting room.
        Threading  = speakers take turns, each holding the mic briefly.
        Asyncio    = one speaker, but they pass the mic while waiting for an answer.
        Multiprocessing = multiple meeting rooms, each with their own mic.
"""

# ==============================================================================
# 1. asyncio — single-threaded, cooperative concurrency for I/O
# ==============================================================================
"""
- Single thread — only ONE thing runs at a time
- Tasks voluntarily YIELD control with `await` when waiting for I/O
- Event loop picks up the next ready task while others are waiting
- DOES NOT help with CPU-bound work (still single-threaded)
- Keywords: async def, await, asyncio.run(), asyncio.gather()
"""

import asyncio
import time

# async def marks a coroutine — calling it returns a coroutine object, NOT the result
# You need to await it (or schedule it) to actually run it
async def fetch_user(user_id: int) -> dict:
    print(f"  Fetching user {user_id}...")
    await asyncio.sleep(1)          # simulates a DB/API call — releases control here
    print(f"  Done fetching user {user_id}")
    return {"id": user_id, "name": f"User_{user_id}"}

# --- Sequential vs Concurrent ---

async def fetch_sequential():
    """Each fetch waits for the previous one to finish. Total: ~3 seconds."""
    start = time.perf_counter()
    u1 = await fetch_user(1)        # waits 1s
    u2 = await fetch_user(2)        # waits another 1s
    u3 = await fetch_user(3)        # waits another 1s
    elapsed = time.perf_counter() - start
    print(f"Sequential took: {elapsed:.2f}s")  # ~3.0s

async def fetch_concurrent():
    """All three fire at once. Total: ~1 second."""
    start = time.perf_counter()
    # gather() schedules all coroutines and runs them concurrently
    # returns results in the same order as the arguments
    u1, u2, u3 = await asyncio.gather(
        fetch_user(1),
        fetch_user(2),
        fetch_user(3),
        return_exceptions=True  # optional: if True, exceptions are returned in results instead of raised
    )
    elapsed = time.perf_counter() - start
    print(f"Concurrent took: {elapsed:.2f}s")  # ~1.0s
    return [u1, u2, u3]

print("=== asyncio: Sequential ===")
asyncio.run(fetch_sequential())     # asyncio.run() is the entry point — starts the event loop

print("\n=== asyncio: Concurrent with gather() ===")
asyncio.run(fetch_concurrent())


# --- async/await mechanics ---

async def demonstrate_await():
    """
    await pauses THIS coroutine and gives control back to the event loop.
    The event loop runs other tasks until the awaited thing is ready.
    """
    print("Step 1 — before await")
    result = await asyncio.sleep(0.5)   # control yields here
    print("Step 2 — after await (0.5s later)")
    return result

# asyncio.create_task() schedules a coroutine to run SOON (non-blocking)
# vs await which runs it RIGHT NOW (blocking this coroutine until done)
async def task_vs_await():
    # create_task: schedules it, doesn't wait
    task = asyncio.create_task(fetch_user(99))
    print("Task created — not waiting yet, doing other work...")
    await asyncio.sleep(0)             # yield control so task can start
    result = await task                # NOW wait for the result
    print(f"Task result: {result}")

asyncio.run(task_vs_await())


# ==============================================================================
# REAL-WORLD asyncio: Async HTTP calls with aiohttp
# ==============================================================================
"""
Classic use case: fetch data from multiple API endpoints simultaneously.

    pip install aiohttp

Instead of calling 5 APIs sequentially (5s total), gather() fires them
all at once and collects results when they're all done (~1s total).
"""

# NOTE: This block is written to run — swap in real URLs for live testing
async def fetch_url(session, url: str) -> str:
    """In real code: async with session.get(url) as resp: return await resp.json()"""
    await asyncio.sleep(0.8)           # simulates network latency
    return f"Response from {url}"

async def fetch_all_apis():
    urls = [
        "https://api.example.com/users",
        "https://api.example.com/orders",
        "https://api.example.com/products",
        "https://api.example.com/reviews",
        "https://api.example.com/inventory",
    ]

    # Real aiohttp usage:
    # async with aiohttp.ClientSession() as session:
    #     results = await asyncio.gather(*[fetch_url(session, url) for url in urls])

    # Simulated version:
    start = time.perf_counter()
    results = await asyncio.gather(*[fetch_url(None, url) for url in urls]) # * unpacks the list into separate arguments
    elapsed = time.perf_counter() - start

    print(f"\nFetched {len(urls)} APIs in {elapsed:.2f}s (would be ~{len(urls)}s sequentially)")
    for r in results:
        print(f"  {r}")

asyncio.run(fetch_all_apis())


# ==============================================================================
# 2. threading — OS threads, good for I/O, limited by GIL for CPU
# ==============================================================================
"""
- Multiple threads share the same memory space
- GIL means only one runs Python bytecode at a time
- Threads still help for I/O because they release the GIL while waiting
- Use when: working with libraries that don't support async (e.g. requests, psycopg2)
- Watch out for: race conditions when threads share mutable state
"""

import threading

# --- Basic thread usage ---
def download_file(filename: str, duration: float):
    """Simulates a blocking I/O operation (e.g. requests.get)."""
    print(f"  Starting download: {filename}")
    time.sleep(duration)              # blocking sleep — releases GIL
    print(f"  Finished download: {filename}")

print("\n=== threading: Sequential (no threads) ===")
start = time.perf_counter()
download_file("file_a.zip", 1.0)
download_file("file_b.zip", 1.0)
download_file("file_c.zip", 1.0)
print(f"Sequential: {time.perf_counter() - start:.2f}s")  # ~3.0s

print("\n=== threading: Concurrent (with threads) ===")
start = time.perf_counter()

threads = [
    threading.Thread(target=download_file, args=("file_a.zip", 1.0)),
    threading.Thread(target=download_file, args=("file_b.zip", 1.0)),
    threading.Thread(target=download_file, args=("file_c.zip", 1.0)),
]

for t in threads:
    t.start()           # launch all threads

for t in threads:
    t.join()            # wait for ALL threads to finish before continuing

print(f"Threaded: {time.perf_counter() - start:.2f}s")  # ~1.0s


# --- Race condition — what happens without a Lock ---
counter = 0

def increment_unsafe(n: int):
    global counter
    for _ in range(n):
        counter += 1    # NOT thread-safe: read → modify → write is 3 steps
                        # another thread can interrupt between any of them

# --- Lock — prevents race conditions ---
safe_counter = 0
lock = threading.Lock()

def increment_safe(n: int):
    global safe_counter
    for _ in range(n):
        with lock:          # only one thread can be inside this block at a time
            safe_counter += 1

threads_safe = [threading.Thread(target=increment_safe, args=(1000,)) for _ in range(5)]
for t in threads_safe: t.start()
for t in threads_safe: t.join()
print(f"\nSafe counter (expected 5000): {safe_counter}")   # always 5000


# --- daemon=True — thread dies when main program exits ---
def background_logger():
    while True:
        time.sleep(2)
        print("  [background] still running...")

logger_thread = threading.Thread(target=background_logger, daemon=True)
logger_thread.start()
# daemon thread won't block program from exiting — useful for background tasks


# ==============================================================================
# REAL-WORLD threading: ThreadPoolExecutor for parallel I/O
# ==============================================================================
"""
ThreadPoolExecutor is cleaner than manually managing Thread objects.
submit() returns a Future — a promise of a result.
Use it when you have many I/O tasks and want a thread pool with a size limit.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import requests  # pip install requests — blocking HTTP lib (no async support)

def scrape_page(url: str) -> str:
    """Blocking HTTP call — fine in a thread since it releases the GIL."""
    # Real version: response = requests.get(url); return response.text
    time.sleep(0.5)                    # simulated
    return f"HTML content from {url}"

urls_to_scrape = [f"https://example.com/page/{i}" for i in range(6)]

print("\n=== ThreadPoolExecutor: scraping 6 pages ===")
start = time.perf_counter()

with ThreadPoolExecutor(max_workers=3) as executor:
    # submit() schedules each call and returns a Future immediately
    futures = {executor.submit(scrape_page, url): url for url in urls_to_scrape}

    # as_completed() yields futures as they finish (not in submission order)
    for future in as_completed(futures):
        url = futures[future]
        result = future.result()        # blocks until this specific future is done
        print(f"  Done: {url} -> {len(result)} chars")

print(f"Scraped {len(urls_to_scrape)} pages in {time.perf_counter() - start:.2f}s")


# ==============================================================================
# 3. multiprocessing — separate processes, true parallelism, bypasses GIL
# ==============================================================================
"""
- Each process has its OWN memory space and its OWN GIL
- True parallel execution across multiple CPU cores
- Higher overhead than threads (process creation, data serialization via pickle)
- Data is COPIED between processes, not shared — no race conditions by default
- Use when: CPU-bound work that needs to scale across cores
"""

import multiprocessing
import os

def cpu_heavy_task(n: int) -> int:
    """Pure CPU work — summing a large range. GIL makes threading useless here."""
    return sum(i * i for i in range(n))

print("\n=== multiprocessing: CPU-bound task ===")

# Sequential
start = time.perf_counter()
results_seq = [cpu_heavy_task(5_000_000) for _ in range(4)]
print(f"Sequential (4 tasks): {time.perf_counter() - start:.2f}s")

# Parallel — uses all available CPU cores
start = time.perf_counter()
with multiprocessing.Pool(processes=4) as pool:
    # map() distributes the list across the pool, blocks until all done
    results_par = pool.map(cpu_heavy_task, [5_000_000] * 4)
print(f"Multiprocessing (4 tasks): {time.perf_counter() - start:.2f}s")
# On a 4-core machine this is ~4x faster


# --- Process with shared state — requires explicit shared memory ---
# Ordinary Python variables are NOT shared between processes (memory is copied)

def worker_with_shared(shared_val, lock):
    with lock:
        shared_val.value += 1
        print(f"  Process {os.getpid()} incremented to {shared_val.value}")

shared_counter = multiprocessing.Value("i", 0)   # "i" = signed int
mp_lock = multiprocessing.Lock()

processes = [
    multiprocessing.Process(target=worker_with_shared, args=(shared_counter, mp_lock))
    for _ in range(4)
]
for p in processes: p.start()
for p in processes: p.join()
print(f"\nShared counter after 4 processes: {shared_counter.value}")  # 4


# ==============================================================================
# REAL-WORLD multiprocessing: ProcessPoolExecutor for image processing
# ==============================================================================
"""
ProcessPoolExecutor is the clean API for multiprocessing (mirrors ThreadPoolExecutor).
Use it for CPU-heavy batch jobs: image resizing, data transformation, ML inference.
"""

from concurrent.futures import ProcessPoolExecutor

def process_image(image_id: int) -> dict:
    """Simulates CPU-heavy image resizing/transformation."""
    # Real version: PIL.Image.open(...).resize(...).save(...)
    result = sum(i ** 2 for i in range(500_000))   # fake CPU work
    return {"image_id": image_id, "checksum": result % 9999}

if __name__ == "__main__":
    # IMPORTANT: multiprocessing code MUST be inside `if __name__ == "__main__"`
    # on Windows/macOS — otherwise spawned processes re-import the module and
    # re-run your top-level code, causing infinite process spawning.

    image_ids = list(range(8))
    print("\n=== ProcessPoolExecutor: processing 8 images ===")
    start = time.perf_counter()

    with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        futures = {executor.submit(process_image, img_id): img_id for img_id in image_ids}
        for future in as_completed(futures):
            print(f"  Processed: {future.result()}")

    print(f"Processed {len(image_ids)} images in {time.perf_counter() - start:.2f}s")


# ==============================================================================
# SIDE-BY-SIDE COMPARISON
# ==============================================================================
"""
Feature               asyncio              threading            multiprocessing
────────────────────────────────────────────────────────────────────────────────
Concurrency model     Cooperative          Preemptive           True parallel
Threads/Processes     1 thread             Multiple threads     Multiple processes
Bypasses GIL          N/A (1 thread)       No                   Yes
Best for              I/O (async libs)     I/O (blocking libs)  CPU-bound work
Memory                Shared               Shared               Separate (copied)
Race conditions       Rare (1 thread)      Yes — use Lock       No (separate mem)
Overhead              Very low             Low                  High (process spawn)
Communication         return / queue       Shared variables     Queue / Pipe / Value
Entry point           asyncio.run()        Thread.start()       Pool.map() / Process
Pool API              asyncio.gather()     ThreadPoolExecutor   ProcessPoolExecutor
Data serialization    Not needed           Not needed           pickle (automatic)
Keyword               async / await        (none)               if __name__ == main

RULES OF THUMB:
  - Network calls, DB queries, file I/O  → asyncio (if lib supports it) else threading
  - Image processing, ML, number crunch  → multiprocessing
  - Quick parallel I/O with old libs     → ThreadPoolExecutor
  - CPU tasks across cores               → ProcessPoolExecutor
  - Never use threading for CPU work     → GIL kills the benefit
"""