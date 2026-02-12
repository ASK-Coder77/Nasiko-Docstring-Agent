import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

    def complex_operation(self, x):
        def internal_helper(n):
            return n * 2
        
        return internal_helper(x) + 10