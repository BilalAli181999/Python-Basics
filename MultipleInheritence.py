class Polygon:
    _width=0
    _height=0
    def __init__(self,h,w):
        self._width=w
        self._height=h
        print("Polygon Constructor")
    def setValues(self,h,w):
        self._height=h
        self._width=w   

class Shape:
    def __init__(self,str):
        print("Shapes Constructor")
        self._color=str
    def get_Color(self):
        return self._color


class Rectangle(Shape,Polygon):
     __area=0
     def __init__(self):
            __area=0
            print("Rectangle Constructor") 

     def get_Area(self):
         print(self._color)
         return self._width*self._height


class Triangle(Polygon,Shape):
     __area=0
     def __init__(self, *args, **kwargs):
            __area=0
            print("Traingle Constructor")
     def get_Area(self):
         return (self._width*self._height)/2



    
rect=Rectangle("yellow")
rect.get_Area()
print(rect._color)