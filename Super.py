class Parent1:
    def __init__(self,str):
        print("Parent1",str)

class Parent2:
    def __init__(self,str):
        print("Parent2",str)

class Child(Parent1,Parent2):
    def __init__(self):
        print("Child")
        super().__init__("Super")    #It only calls one parent that is on left side
        Parent1.__init__(self,"First")
        Parent2.__init__(self,"Second")

#p1=Parent1()                
c=Child()