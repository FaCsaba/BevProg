#!/usr/bin/env python3
# coding: utf8

# Homework: 1
# Pyramids and cones
# Make a function that calculated the base area of a pyramid or cone 
# and use that to calculate the volume

# Representation of a Pyramid 
# arguments are given in units
class Pyramid:
    def __init__(self, base_length: tuple[int, int] | int, height: int):
        if isinstance(base_length, int):
            base_length = (base_length, base_length)

        self.base_side_a = base_length[0]
        self.base_side_b = base_length[1]
        self.height = height
        self.base_area = self.calculate_base_area()
        
        self.volume = (self.base_area * self.height) / 3
    
    def __repr__(self):
        return f"Pyramid:\n\tside a: {self.base_side_a} u\tside b: {self.base_side_b} u\n\theight: {self.height} u\n\tbase area: {self.base_area} u\u00b2\n\tvolume: {self.volume} u\u00b3"
    
    def calculate_base_area(self) -> int:
        return self.base_side_a * self.base_side_b

# representation of a cone
# arguments are given in units
class Cone:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.base_area = self.calculate_base_area()
        
        self.volume = self.base_area * self.height / 3
    
    def calculate_base_area(self) -> float:
        return self.radius * self.radius * 3.14
    
    def __repr__(self):
        return f"Cone:\n\tradius: {self.radius} u\n\theight: {self.height} u\n\tbase area: {self.base_area} u\u00b2\n\tvolume: {self.volume} u\u00b3"
    

def main():
    p = Pyramid(6, 10)
    print(p)    
    c = Cone(6, 9)
    print(c)

if __name__ == "__main__":
    main()