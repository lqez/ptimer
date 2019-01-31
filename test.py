from ptimer import repeat
from datetime import datetime


def foo():
    print("hello", datetime.now())


if __name__ == "__main__":
    repeat(foo, 10)
