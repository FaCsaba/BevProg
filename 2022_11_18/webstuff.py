#!/usr/bin/env python3
# coding: utf8

# Homework 

import urllib.request
import json

def main():
    res = json.loads(urllib.request.urlopen("https://jsonip.com/").read().decode('utf-8'))
    print(res)
    

if __name__ == "__main__":
    main()