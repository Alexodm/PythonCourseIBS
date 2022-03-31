from threading import Thread
from time import sleep


def thread_func(thread_id):
    print(f"Thread number {thread_id} started")
    for i in reversed(range(10)):
        print(f"Thread number {thread_id} output: {i + 1}")
        sleep(1)
    print(f"Thread number {thread_id} finished")


th1 = Thread(target=thread_func(1))
th2 = Thread(target=thread_func(2))
th1.start()
th2.start()
