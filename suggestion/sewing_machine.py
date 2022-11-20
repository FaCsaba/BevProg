#!/usr/bin/env python3
# coding: utf8

class Dimension:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    
    def __eq__(self, o: 'Dimension'):
        if self.height == o.height and self.width == o.width:
            return True
        return False
    
class Character:
    def __init__(self, num_of_lines: int):
        self.num_of_lines = num_of_lines

    def __add__(self, other: 'Character') -> 'Character':
        res = self.num_of_lines + other.num_of_lines
        if res > 4:
            res = 4
        return Character(res)

    def __iadd__(self, other: 'Character') -> 'Character':
        self.num_of_lines += other.num_of_lines
        if self.num_of_lines > 4:
            self.num_of_lines = 4
        return self
        
    def __str__(self) -> str:
        if self.num_of_lines == 0:
            return " "
        if self.num_of_lines == 1:
            return "-"
        if self.num_of_lines == 2:
            return "+"
        if self.num_of_lines == 3:
            return "*"
        else:
            return "●"

class Pattern:
    def __init__(self, pattern: list[list[Character]]) -> Self:
        self.dimension = Dimension(len(pattern[0]), len(pattern))
        self.pattern = pattern
        
        
        
    def fromString(inp: list[str]) -> Self:

        return Pattern(pattern)
        
    def __add__(self, o: 'Pattern'):
        if not self.dimension == o.dimension:
            raise Error("You can't add another pattern if they aren't the same dimension")
        
        res_pattern: list[list[Character]] = []
        for i in range(len(self.pattern)):
            res_line: list[Character] = []
            for j in range(len(self.pattern[i])):
                res_line.append(self.pattern[i][j] + o.pattern[i][j])
            res_pattern.append(res_line)
        return Pattern(res_pattern)
    
    def __str__(self):
        return "\n".join(map(lambda x: "".join(map(lambda x: x.__str__(), x)), self.pattern))
            


def main():
    a = Pattern([[Character(2), Character(1)], [Character(1), Character(1)]])
    b = Pattern([[Character(1), Character(1)], [Character(1), Character(2)]])
    print(a+b)
    
    

if __name__ == "__main__":
    main()