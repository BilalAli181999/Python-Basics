class a:
    attr1=0
    def __init__(self):
        self.attr1=10
        print("Constructor")
    def printA(self):
        print(self.attr1)

#def a():
 #   print("hello world")


A=a()
A.printA()