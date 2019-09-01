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