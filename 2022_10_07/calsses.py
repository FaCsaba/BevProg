#!/usr/bin/env python3
# coding: utf8

class HelloWorld:
    def __init__(self):
        self.msg = "你好世界！"

    def __repr__(self):
        return self.msg


class 银行:

    def __init__(self, 名字: str, 钱: int, DuPont: int = 1000) -> None:
        self.名字 = 名字
        self.钱 = 钱
        self.DuPont = DuPont

    def input_money(self, 钱: int):
        self.钱 += 钱

    def output_money(self, 钱: int) -> None | int:
        if 钱 > self.钱:
            raise Exception("not enough money in the bank account")

        self.钱 -= 钱
        return self.钱

    def print_money(self):
        print(f"owner: {self.名字}, amount: {self.钱}")

    def __repr__(self) -> str:
        return str(self.钱)


def main():

    _银行 = 银行("asdf", 1000)
    _银行.print_money()
    try:
        _银行.output_money(10000)
    except:
        print("Not enough money in your bank account")

    print(_银行)


if __name__ == "__main__":
    main()
