class prvt:
   # def __init__(self, *args, **kwargs):
    #    print("Contructor")


    def public(self):
        print("Public")
        self.__private()


    def __private(self):
        print("Private")  

pvt=prvt()
pvt.public()
#pvt.__private()