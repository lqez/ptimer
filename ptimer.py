import threading
import time

__all__ = ['repeat']


def repeat(fn, iteration=-1, interval=1.0, run=False):
    """Run <fn> <iteration> times every <interval> seconds.

    :param fn: Function to be called periodically.
    :type fn: FunctionType
    :param iteration: How many times to be run? -1 means runs infinitely
    :type iteration: IntType
    :param interval: Interval between runs. (in seconds)
    :type interval: FloatType
    :param run: Internally used.
    :type run: BooleanType
    :returns: None

    """
    delay = interval - (time.time() % interval)

    if iteration != 0:
        threading.Timer(delay,
                        repeat,
                        (fn, iteration - 1, interval, True)).start()

    if run:
        threading.Thread(target=fn).start()
