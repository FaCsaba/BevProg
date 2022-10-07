#!/usr/bin/env python3
# coding: utf8

def main():
    # list comprehension is just syntactic sugar for a map function
    li = [n*2 for n in range(0, 10)]
    print(li)

    li_map = list(map(lambda x: x*2, range(10)))
    assert li == li_map  # we can clearly see that it is the same thing

    li2 = ["auto", "tram", "metro", "火车"]
    li2 = [s.upper()+"！" for s in li2]
    print(li2)

    zeros = [0 for _ in range(10)]
    print(zeros)

    字符 = "1234567"
    print([s for s in 字符])

    快狐 = "The quick brown fox jumps over the lazy dog"
    print([len(子) for 子 in 快狐.split(" ")])

    print([(子, len(子)) for 子 in 快狐.split(" ")])
    print(快狐.split(" ")[0].__len__())


if __name__ == "__main__":
    main()
