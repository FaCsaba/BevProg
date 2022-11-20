#!/usr/bin/env python3
# coding: utf8

# Homework Pi

import os

N_TH_PI_NUMBER = 0

def main():
    with open(os.path.join(os.path.dirname(__file__), "PI_POEM"), "r") as inp, open(os.path.join(os.path.dirname(__file__), "PI_POEM_OUT"), "w") as out:
        print([len(x) for x in inp.read().split()][N_TH_PI_NUMBER], file=out)

if __name__ == "__main__":
    main()