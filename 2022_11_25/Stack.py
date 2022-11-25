#!/usr/bin/env python3
# coding: utf8

# Stack

class Stack:
    def __init__(self, initial: list = []):
        self._s = initial
    
    def put_in(self, item: any):
        self._s.append(item)
        
    def get_out(self):
        return self._s.pop()
    
    def length(self):
        return len(self._s)

    def is_empty(self):
        return len(self._s) == 0

    def __repr__(self):
        return "[ " + " ".join([repr(x) for x in self._s])
    
    def __len__(self):
        return self.length()
        
def debug():
    s = Stack()
    s.put_in(1)
    s.put_in(5)
    s.put_in(3)
    s.put_in(69)
    s.put_in([])
    print(s.length())
    print(s.get_out())

if __name__ == "__main__":
    debug()