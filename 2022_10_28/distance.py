#!/usr/bin/env python3
# coding: utf8

from enum import Enum


class Field(Enum):
    GARDEN = 0,
    TREE = 1,
    HOUSE = 2,
    PARK = 3,


class Place:
    def __init__(self, start_pos: int, end_pos: int, type_of_field: Field = Field.GARDEN):
        self.begin = min(start_pos, end_pos)
        self.end = max(start_pos, end_pos)
        self.type = type_of_field

    def distance(self):
        return self.end - self.begin

    def __str__(self):
        return f"({self.begin};{self.end})"

    def __add__(self, other: 'Place') -> 'Place':  # we need another place to add to self
        return Place(min(self.begin, other.begin), max(self.end, other.end))

    def __sub__(self, other: 'Place') -> 'Place':
        return Place(max(self.begin, other.begin), min(self.end, other.end))

    def __ge__(self, other: 'Place'):  # greater equal then  a >= b
        if self.distance() >= other.distance():
            return True
        return False

    def __le__(self, other: 'Place'):
        if self.distance() <= other.distance():
            return True
        return False

    def __gt__(self, other: 'Place'):
        if self.distance() > other.distance():
            return True
        return False

    def __lt__(self, other: 'Place'):
        if self.distance() < other.distance():
            return True
        return False

    def __eq__(self, other: 'Place'):
        if self.distance() == other.distance():
            return True
        return False

    def __iadd__(self, b: int):
        self.end += b
        return self

    def __isub__(self, b: int):
        self.begin -= b
        return self


def main():
    p1 = Place(8, 5)
    p2 = Place(2, 9)

    print(p1)
    print(p1 == p2)
    print(p1 - p2)
    p1 += 1
    print(p1)

    pass


if __name__ == "__main__":
    main()
