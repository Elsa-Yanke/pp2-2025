class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.length =  length
        self.width = width
    
    def area(self):
        return self.length * self.width
rectangle = Rectangle(6, 8)