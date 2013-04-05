import threading
import time

__all__ = ['repeat']


def repeat(fn, iteration=-1, interval=1.0, run=False):
    delay = interval - (time.time() % interval)

    if iteration != 0:
        threading.Timer(delay, repeat, (fn, iteration - 1, interval, True)).start()

    if run:
        threading.Thread(target=fn).start()
