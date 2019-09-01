from Polygon import Polygon 

class Triangle(Polygon):
     __area=0
     def __init__(self, *args, **kwargs):
            __area=0
            print("Traingle Constructor")
     def get_Area(self):
         return (self._width*self._height)/2

