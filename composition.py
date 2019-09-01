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
    def __init__(self, name,age,pay,bonus):
        self.name=name
        self.age=age
        self.__obj_sal=Salary(pay,bonus)
        print("Employee's Constructor")
    def getAnnualEarning(self):
        return self.__obj_sal.getAnnualPay()    
  

emp=Employee("Bilal",20,80000,300000)
print(emp.getAnnualEarning())  
#print(emp.__obj_sal.getAnnualPay())