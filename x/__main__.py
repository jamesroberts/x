import pickle
from multiprocessing.shared_memory import SharedMemory
from x.shared_cache import SharedCache
import numpy as np
import os
import signal
import bjoern
import json

from x.app import init_app

NUM_WORKERS = os.cpu_count()
HOST = "0.0.0.0"
PORT = 5000

workers = []

print(f"Starting WSGI on {HOST}:{PORT}")

bjoern.listen(init_app(), HOST, PORT)

main_pid = os.getpid()
print(f"Main worker on PID {main_pid}")

KB_64 = 1024*64
cache = SharedCache(name="sharedcache")
print("Cache started")

for _ in range(NUM_WORKERS):
    pid = os.fork()
    if pid > 0:
        workers.append(pid)
        print(f"Worker process added with PID: {pid}")
    else:
        try:
            bjoern.run()
        except KeyboardInterrupt:
            exit()

try:
    for _ in range(NUM_WORKERS):
        os.wait()
except KeyboardInterrupt:
    print("Stopping all workers")
    for worker in workers:
        cache.close()
        os.kill(worker, signal.SIGINT)
        try:
            cache.unlink()
        except FileNotFoundError:
            pass
