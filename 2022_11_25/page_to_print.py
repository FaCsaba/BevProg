#!/usr/bin/env python3
# coding: utf8

# Page to print

def flatten(n: list) -> list:
    ret_l = []
    for x in n:
        for item in x:
            ret_l.append(item)
    return ret_l

def get_pages_to_print(n: str):
    pages = []
    for p in n.split(','):
        p = p.split('-')
        if len(p) > 1:
            pages.append(list(range(int(p[0]), int(p[1]) + 1)))
            pass
        else:
            pages.append([int(p[0])])
    return set(flatten(pages))

def main():
    pages_to_print_str = "1,1-5,9-99"
    print(get_pages_to_print(pages_to_print_str))

if __name__ == "__main__":
    main()