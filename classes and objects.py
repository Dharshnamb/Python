"""
class goa:
    name="Not registered"
    drink=""                                          #goa is class
    def party(self):
        print("Lets party...")
    def beach(self):
        print("Enjoy the beach")

ramesh = goa()
suresh = goa()                                       #ramesh and suresh are objects

ramesh.name="Ramesh"
suresh.name="Suresh"

ramesh.drink="YES"
suresh.drink="NO"

print(ramesh.name)
print("Drink:",ramesh.drink)
ramesh.party()

print(suresh.name)
print("Drink:",suresh.drink)
suresh.beach()
"""
"""
class laptop:
    price=""
    processor=""
    ram=""
   
hp=laptop()
dell=laptop()
lenovo=laptop()

hp.price=57000
hp.processor="i5"
hp.ram="8gb"

dell.price=56000
dell.processor="i7"
dell.ram="8gb"

lenovo.price=50000
lenovo.processor="i5"
lenovo.ram="16gb"

print(hp.price)
"""
#CONSTRUCTOR AND SELF KEYWORD
"""
class laptop:
    def __init__(self):                        #a constructor is a unique function that gets called automatically when an object is created of a class
        self.price=0
        self.ram=""
        self.processor=""
    def display(self):                         #must add self in functions inside class
        print("Ram:",self.ram)
        print("Processor:",self.processor)     #used to denote current object
hp=laptop()

hp.price=57000
hp.processor="i5"
hp.ram="8gb"

print(hp.price)
hp.display()
"""
"""
class student:
    def __init__(self):
        self.name="dharsh"
        self.regno="12344"
    def display(self):
        print("Name:", self.name)
        print("Reg.no:",self.regno)
s1=student()
s2=student()

s1.name="Manoj"
s1.regno="12345"

s2.name="Karthi"
s2.regno="23456"

print(s1.name)
print(s1.regno)
s1.display()
s2.display()
"""
"""
class fruit:
    def __init__(self,col):                      #passing variable as parameter through object
        self.color=col
apple=fruit("red")
print(apple.color)
"""
"""
class teacher:
    def __init__(self,nam,reg):                  #passing multiple variables as parameters
        self.name=nam
        self.regno=reg
    def display(self):
        print("Name:",self.name)
        print("RegNo:",self.regno)
t1=teacher("mahes","7123")
t1.display()
t2=teacher("ragavi","7124")
t2.display()
"""
"""
class calculator:
    def __init__(self,a,b):                     #doing diff arithmetic operations using passing parameters
        self.a=a
        self.b=b
    def add(self):
        print(a+b)
    def sub(self):
        print(a-b)
    def mul(self):
        print(a*b)
    def div(self):
        print(a/b)

a=int(input("Enter a:"))
b=int(input("Enter b:"))
c1=calculator(a,b)
c1.sub()
"""
#TYPE OF CLASS VARIABLES
"""
class phone:
    chargertype="ctype"                         #class variable
    def __init__(self,brand,price):
        self.brand=brand                        #instance variable
        self.price=price                        #insatnce variable
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Chargertype:",self.chargertype)

phone.chargertype="btype"
samsung=phone("Samsung","150000")
samsung.display()
"""
#TYPES OF CLASS METHODS
"""
class laptop:
    chargertype="ctype"

    def __init__(self):                           
        self.brand=""
        self.price="100000"
    def setprice(self,price):
        self.price=price
    def getprice(self):                             #instance method
        print(self.price)
    @classmethod                                    #class method
    def changechargertype(cls):
        cls.chargertype="ctype"
        print("Chargertype changed to c")
    @staticmethod
    def info():                                     #static method
        print("This is laptop class")

hp=laptop()
hp.setprice("150000")
hp.getprice()
laptop.changechargertype()
hp.info()
"""














































