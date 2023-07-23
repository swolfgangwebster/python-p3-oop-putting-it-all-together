#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    def get_size(self):
        return self._size
    
    def set_size(self, s):
        if type(s) != int:
            print("size must be an integer")
        self._size = s

    size = property(get_size, set_size)

    pass