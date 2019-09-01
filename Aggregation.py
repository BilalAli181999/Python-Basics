class Salary:
    pay=0
    bonus=0

    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
        print("Salary Constructor")
    def getAnnualPay(self):
        return self.pay*12+self.bonus    

class Employee:
    name=""
    age=""
    __obj_sal=None
    def __init__(self, name,age,sal):
        self.name=name
        self.age=age
        self.__obj_sal=sal
        print("Employee's Constructor")
    def getAnnualEarning(self):
        return self.__obj_sal.getAnnualPay()    
  
sal=Salary(80000,300000)
emp=Employee("Bilal",20,sal)
print(emp.getAnnualEarning())  
#print(emp.__obj_sal.getAnnualPay())