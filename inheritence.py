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


class Rectangle(Polygon):
     __area=0
     def __init__(self, *args, **kwargs):
        __area=0
        print("Rectangle Constructor") 
     def get_Area(self):
         return self._width*self._height


class Triangle(Polygon):
     __area=0
     def __init__(self, *args, **kwargs):
            __area=0
            print("Traingle Constructor")
     def get_Area(self):
         return (self._width*self._height)/2


#Geeks for Geeks Example

class Person(object): 
       
    # Constructor 
    def __init__(self, name): 
        print("Base Constructor",name)
        self.name = name 
   
    # To get name 
    def getName(self): 
        return self.name 
   
    # To check if this person is employee 
    def isEmployee(self): 
        return False
   
   
# Inherited or Sub class (Note Person in bracket) 
class Employee(Person): 
   
    # Here we return true 
    def isEmployee(self): 
        return True
   
# Driver code 
#emp = Person("Geek1")  # An Object of Person 
#print(emp.getName(), emp.isEmployee()) 
   
#emp = Employee("Geek2") # An Object of Employee 
#print(emp.getName(), emp.isEmployee()) 



rect=Rectangle(10,20)  
print(rect.get_Area())       
                 



