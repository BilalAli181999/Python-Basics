class a:
    attr1=0
    

    def __init__(self,a):
        self.attr1=a
        print("Constructor",a)  

    def __init__(self):
        print("Constructor")      
   

#con=a()    #only one constructor works which is the last one and remaining are overwritten

class b:
    attr1=0
    

    def __init__(self,a=1):
        self.attr1=a
        print("Constructor",a)  

       
   
#ex2=b()     #In this way it works for both
#ex3=b(12)


class args:
    def __init__(self,*args):
        for i in args:
          print(i)      
       
   
#multiple=args()
#m2=args(1,2)
#m3=args('a',"b",'c',"d")

class dict:
    def __init__(self,*args,**kwargs):
        print("List")
        for i in args:
            print(i)
        print("Dictionary")    
        for key in kwargs: 
            print (key,kwargs[key]) 
bilal =	{
  "age": 20,
  "height": "5'7",
  "year": 1999

}
#ex=dict( first =1, mid ='for', last='Geeks')
#ex5=dict(1,2,3,a=1,b=2)
ex6=dict(bilal)