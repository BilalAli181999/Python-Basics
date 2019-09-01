class A:
    a=[]
    
    def __init__(self, *args, **kwargs):
        self.__b=10
        for i in args:
          self.a.append(i)
    def get_list(self):
        return self.a
    def dsiplay_list(self):
        for i in self.a:
            print(i)   
    def get_b(self):
        return self.__b         


l=A(1,2,3,4,5,6) 
l.dsiplay_list()
listA=l.get_list()        
print(listA)
print(l.get_b())