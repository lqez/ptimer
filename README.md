ptimer
======

Yet another precision timer for Python

- Support better precision than just using sleep() in a loop.
- Will be fired at almost **exact** timing. (e.g: not 12:00:00.358, exact 12:00:00.000)


BENCHMARK
=========

[Benchmark of sleep vs ptimer](https://docs.google.com/spreadsheet/ccc?key=0Anva4clMXVtVdFF6M0hvdFZDalFyVmEtMGtMdDVSQ1E#gid=0)



INSTALL
=======

    $ pip install ptimer


USAGE
=====

    from ptimer import repeat
    from datetime import datetime


    def foo():
        print "hello", datetime.now()


    if __name__ == "__main__":
        repeat(foo, 10)
