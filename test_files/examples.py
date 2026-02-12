import math

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_factorial(n):
    if n == 0:
        return 1
    return n * get_factorial(n - 1)

class ShapeProcessor:
    def __init__(self, name):
        self.name = name

    def circle_area(self, radius):
        return math.pi * (radius ** 2)

    def rectangle_perimeter(self, length, width):
        return 2 * (length + width)

    def process_data(self, data_list):
        def validate(item):
            return item > 0
        
        return [x for x in data_list if validate(x)]

class DataVisualizer:
    async def fetch_and_plot(self, source_url):
        # Simulated async method
        pass