import os
import signal
import bjoern

from x.app import init_app

NUM_WORKERS = 8
HOST = "0.0.0.0"
PORT = 5000

workers = []

print(f"Starting WSGI on {HOST}:{PORT}")
bjoern.listen(init_app(), HOST, PORT)
for _ in range(NUM_WORKERS):
    pid = os.fork()
    if pid > 0:
        print(f"Worker process added with PID: {pid}")
        workers.append(pid)
    else:
        try:
            bjoern.run()
        except KeyboardInterrupt:
            pass
        exit()

try:
    for _ in range(NUM_WORKERS):
        print("Workers waiting")
        os.wait()
except KeyboardInterrupt:
    print("Stopping all workers")
    for worker in workers:
        os.kill(worker, signal.SIGINT)
