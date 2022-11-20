#!/usr/bin/env python3
# coding: utf8

# Json-ozgatas

import json

def main():
    with open("simple.json", "r") as f:
        s = json.load(f)
        print(s)

    people = {}
    with open("more_people.json", "r") as f:
        c = json.loads(f.read())
        for p in c['people']:
            p['name'] = "ditto"
        people = c
    with open("more_people.json", "w") as f:
        json.dump(c, f, indent=4)
    
if __name__ == "__main__":
    main()