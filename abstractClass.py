from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):pass
    @abstractmethod
    def perimeter(self):pass

class Square(Shape):
    def __init__(self):
        print("Shapes Contructor")
    def area(self):
        return 1 
    def perimeter(self):
        return 1

s=Square()