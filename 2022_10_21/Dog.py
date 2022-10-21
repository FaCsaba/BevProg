#!/usr/bin/env python3
# coding: utf8

# Making a Dog (his name will be Dough)

class Dog:
    def __init__(self, name: str, type: str, age_in_human_years: int):
        self.name = name
        self.type = type
        self._age = age_in_human_years

    def getAge(self):
        self._age

    def setAge(self, age: int):

        if age >= 0:
            self._age = age
        else:
            raise Exception("Incorrect number for age")

    def __str__(self):
        return f"{self.name} egy {self.type} kutya aki {self._age * 7} éves!"


def ugat(dog: Dog):
    print(f"{dog.name}: VÁÚ")


def ask_for_int(inp_message: str) -> int:
    while True:  # simple error handling. if user provides incorrect data we loop until we get a number
        try:
            inp = input(inp_message)
            return int(inp)
        except ValueError as err:
            print("{inp} is not a number".format(inp=inp))
            continue


def ask_for_str(inp_message: str) -> str:
    while True:  # simple error handling. if user provides incorrect data we loop until we get a number
        try:
            inp = input(inp_message)
            return str(inp)
        except ValueError as err:
            print("{inp} is not a number".format(inp=inp))
            continue


def main():
    dogs: List(Dog) = []
    for x in range(3):
        dogs.append(Dog(ask_for_str("Név: "), ask_for_str(
            "Fajta: "), ask_for_int("Kor: ")))

    for dog in dogs:
        ugat(dog)


if __name__ == "__main__":
    main()
