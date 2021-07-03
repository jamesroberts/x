import os
import signal
import bjoern

from x.app import init_app

NUM_WORKERS = os.cpu_count()
HOST = "0.0.0.0"
PORT = 5000

workers = []

print(f"Starting WSGI on {HOST}:{PORT}")

bjoern.listen(init_app(), HOST, PORT)

main_pid = os.getpid()
print(f"Main worker on PID {main_pid}")


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
        os.kill(worker, signal.SIGINT)
