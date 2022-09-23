#!/usr/bin/env python3
# coding: utf8
# Tuples are lovely

def _tuple(): 
    kartya = (1, "Priscilla", 4.5)
    id, nev, jegy = kartya
    print(kartya)
    print(id)
    print(nev)
    print(jegy)

def _dict():    
    osztalyzat = {"Anna": 2.5, "Bela": 2, "Cecilia": 1}
    osztalyzat["Anna"] = 5
    print(osztalyzat)

    print(osztalyzat.keys())
    print(osztalyzat.values())
    print(osztalyzat.items())

if __name__ == "__main__":
    _tuple()
    _dict()