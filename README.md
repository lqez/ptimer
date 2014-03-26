ptimer
======

Yet another precision timer for Python

- Support better precision than just using sleep() in a loop.
- Will be fired at almost **exact** timing. (e.g: not 12:00:00.35, exact 12:00:00.00)


BENCHMARK
---------

[Benchmark of sleep vs ptimer](https://docs.google.com/spreadsheet/ccc?key=0Anva4clMXVtVdFF6M0hvdFZDalFyVmEtMGtMdDVSQ1E&usp=sharing)


INSTALL
-------

    $ pip install ptimer


USAGE
-----

    from ptimer import repeat
    from datetime import datetime


    def foo():
        print "hello", datetime.now()


    if __name__ == "__main__":
        repeat(foo, 10)

... And its result

    $ python test.py
    hello 2013-04-09 02:41:57.003137
    hello 2013-04-09 02:41:58.006444
    hello 2013-04-09 02:41:59.004457
    hello 2013-04-09 02:42:00.002213
    hello 2013-04-09 02:42:01.002505
    hello 2013-04-09 02:42:02.002114
    hello 2013-04-09 02:42:03.002309
    hello 2013-04-09 02:42:04.003766
    hello 2013-04-09 02:42:05.001562
    hello 2013-04-09 02:42:06.002660
    

DOCUMENT
--------

```
# Run <fn> <iteration> times every <interval> seconds.
def repeat(fn, iteration=-1, interval=1.0, run=False)
```
