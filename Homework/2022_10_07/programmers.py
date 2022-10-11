#!/usr/bin/env python3
# coding: utf8

# Homework Programmers

from enum import Enum


class Rank(Enum):
    Intern = 0
    Junior = 1
    Medior = 2
    Senior = 3


class Programmer:
    def __init__(self, name: str, compensation: int, rank: Rank = Rank.Junior, years_worked: int = 0):
        self.name = name
        self.rank = rank
        self.years_worked = years_worked
        self.compensation = compensation

    def increase_compensation(self, inc_with: int = 10_000):
        self.compensation += inc_with

    def worked_a_year(self):
        self.years_worked += 1
        self.calculate_rank()

    def calculate_rank(self):
        if self.years_worked > 1:
            self.rank = Rank.Intern
        if 1 < self.years_worked < 2:
            self.rank = Rank.Junior
        if 2 < self.years_worked < 5:
            self.rank = Rank.Medior
        else:
            self.rank = Rank.Senior

    def __repr__(self) -> str:
        return f"Programmer {self.name}, {self.rank}:\nmakes: {self.compensation}\tworked for: {self.years_worked} years"


def test():
    j = Programmer("John Dough", 1000, years_worked=4)
    assert j.name == "John Dough"
    assert j.rank == Rank.Junior
    j.calculate_rank()
    assert j.rank == Rank.Medior
    j.worked_a_year()
    assert j.rank == Rank.Senior
    j.increase_compensation(100)
    assert j.compensation == 1100


if __name__ == "__main__":
    test()
