#!/usr/bin/env python3
# coding: utf8

# Sys

import sys
import os

def main():
    print(os.environ['PATH'].split(':'))
    print(sys.argv)

if __name__ == "__main__":
    main()