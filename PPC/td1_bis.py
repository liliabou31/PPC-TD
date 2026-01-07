import os
import time
import signal
from multiprocessing import Process

def child_task(parent_pid):
    print(f"Child PID: {os.getpid()}, Parent PID: {parent_pid}")
    print("Child sleeping for 5 seconds...")
    time.sleep(5)
    print("Child sending SIGUSR1 to parent")
    os.kill(parent_pid, signal.SIGUSR1)
    # Sleep indefinitely (will be killed by parent)
    while True:
        time.sleep(1)

def parent_signal_handler(signum, frame):
    print(f"Parent received signal: {signum}")
    print(f"Parent PID: {os.getpid()}, killing child PID: {child.pid}")
    os.kill(child.pid, signal.SIGKILL)  # terminate the child
    print("Child killed")
    exit(0)

if __name__ == "__main__":
    # Set up the parent signal handler
    signal.signal(signal.SIGUSR1, parent_signal_handler)

    print(f"Parent PID: {os.getpid()}")
    child = Process(target=child_task, args=(os.getpid(),))
    child.start()

    # Wait for child to terminate (or be killed)
    child.join()
    print("Parent exiting")
