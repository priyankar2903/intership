'''class sum:
    def getdata(self):
        self.num=int(input("enter number"))
        self.num1=int(input("enter number"))
    def calculate(self):
        self.result=self.num+self.num1
    def display(self):
        print("result=",self.result)
obj=sum()
obj.getdata()
obj.calculate()
obj.display()'''        

#evenodd
'''class evenodd:
    def getdata(self):
        self.num=int(input("enter number"))
    def display(self):
        if self.num%2==0:
            print("number is even") 
        else:
            print("number is odd")    
obj=evenodd()
obj.getdata()
obj.display()'''      

'''#addition
class sum:
    def getdata(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def calculate(self):
        self.result=self.num1+self.num2
    def display(self):
        print("result=",self.result)
num=int(input("enter number"))
num1=int(input("enter number"))           
obj=sum()
obj.getdata(num,num1)
obj.calculate() 
obj.display() '''

'''#constructor
class evenodd:
    def __init__ (self):
        self.num=int(input("enter number"))
    def display(self):
        if self.num%2==0:
            print("number is even")
        else:
            print("number is odd")
obj=evenodd()
obj.display()'''

'''class evenodd:
    def __init__(self,num):
        self.num=num
    def display(self):
        if self.num%2==0:
            print("number is even")
        else:
            print("number is odd")
num=int(input("enter number"))
obj=evenodd(num)
obj.display()'''       

'''class sum:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def calculate(self):
        self.result=self.num1+self.num2
    def display(self):
        print("result=",self.result)  
num=int(input("enter number"))
num1=int(input("enter number"))
obj=sum(num,num1)
obj.calculate() 
obj.display()'''            


         