#!/usr/bin/env python3
# coding: utf8

# Point class

from math import sqrt


class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    # def __repr__(self) -> str:
    #     return f"({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def length(self) -> int:
        return sqrt(self.x**2 + self.y**2)

    def diff(self, x, y):
        return Point(x - self.x, y - self.y).length()

    def diff(self, other: 'Point') -> int:
        return Point(other.x - self.x, other.y - self.y).length()


def first_quarter(li: list) -> list:
    li = [p for p in li if p.x > 0 and p.y > 0]
    if len(li) > 0:
        return li[0]
    else:
        return None


def test():
    a = Point(1, 2)
    b = Point(4, 5)
    c = Point(-1, 4)

    print(a.diff(b))
    print(first_quarter([c, a, b]))


if __name__ == "__main__":
    test()
