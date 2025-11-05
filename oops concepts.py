#INHERITANCE AND ITS TYPES
"""
class dad():
    def phone(self):
        print("Dad's phone")
class son(dad):
    def laptop(self):                   #single inheritance
        print("Son's laptop")

ram=son()
ram.laptop()
ram.phone()
"""
"""
class dad():
    def phone(self):
        print("Dad's phone")
class mom():
    def sweet(self):
        print("Mom's sweet")
class son(dad,mom):                     #multiple inheritance
    def laptop(self):                   
        print("Son's laptop")

ram=son()
ram.laptop()
ram.phone()
ram.sweet()
"""
"""
class grandpa():
    def phone(self):
        print("Granpa's phone")
class dad(grandpa):
    def money(self):
        print("Dad's money")
class son(dad):                        #multiple level inheritance
    def laptop(self):
        print("Son's laptop")

ram=son()
ram.laptop()
ram.money()                            #since son linked to dad ram can access money
d1=dad()
d1.money()
d1.phone()                             #since dad linked to grandpa d1 can access phone
ram.phone()                            #since dad linked to grandpa ram can access phone
"""
"""
class dad():
    def money(self):
        print("Dad's money")

class son1(dad):                       #hierarchial inheritance
    pass
class son2(dad):                       #hierarchial inheritance
    pass
class son3(dad):                       #hierarchial inheritance
    pass

s2=son2()
s2.money()
"""
"""
class dad():
    def money(self):
        print("Dad's money")
class land():
    def importantland(self):
        print("important land")

class son1(dad,land):                 #dad,son1,land - multiple inheritance
    pass
class son2(dad):                      #dad,son1,son2,son3 - hierarchial inheritance
    pass
class son3(dad):                      #diff inheritance connected is hybrid inheritance
    pass

s2=son2()
s2.money()
"""
#SUPER KEYWORD
"""
class a():
    def __init__(self):
        print("A")
    def display(self):
        print("You are in class a")
class b(a):
    def __init__(self):
        super().__init__()           #accessing parent class' constructor eventhough there is constructor in itself
        print("B")
    def display(self):
        print("You are in class b")
class c(b,a):
    def __init__(self):
        super().__init__()
        print("C")
    def display(self):
        print("You are in class b")
obj=c()
"""
#POLYMORPHISM- a single func used by diff types(datatypes,no.of arguments)
"""
def add(a,b,c=0):                   #if value is passed it gets occupied in c
    print(a+b+c)

add(1,2)                            #else the value given in func name is used
add(1,2,3)
"""
"""
class animal():
    def sound(self):
        print("Animal makes sound")

class dog(animal):
    def sound(self):               #method overriding - polymorphism
        print("Dog barks")

class bird(animal):
    def sound(self):
        print("Birds sing")

a1=animal()
a1.sound()                         #sound takes - "Animal makes noise"

d1=dog()
d1.sound()                         #sound takes - "Dog barks"

b1=bird()
b1.sound()                         #sound takes - "Birds sing"
"""
#INHERITANCE AND POLYMORPHISM WITH EXAMPLES
"""
class shape():
    def area(self):
        return 0

class rectangle(shape):
    def area(self,a,b):
        return a*b

a=int(input("Enter length:"))
b=int(input("Enter breadth:"))

r1=rectangle()
print(r1.area(a,b))

r2=shape()
print(r2.area())
"""
"""
class person():
    def __init__(self,name):
        self.name=name

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
        
    def display(self):
        print("Name:",self.name)
        print("Grade:",self.grade)

s1=student("Dharshna","90")
s1.display()
"""
"""
class vehicle():
    def start(self):
        print("vehicle started")

class car(vehicle):
    def start(self):
        print("car started")

v1=vehicle()
v1.start()

c1=car()
c1.start()
"""
"""
class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department

    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Department:",self.department)

m1=manager("dharshna","1000000","cse")
m1.display()
"""
#ENCAPSULATION - to secure variables in a class
"""
class company():
    def __init__(self):
        self.__companyname="google"          #access modifier - __ (private variable)
                                             #can be accessed only within the class
    def companyname(self):
        print(self.__companyname)            

c1=company()
c1.companyname()
print(c1.__companyname)
"""
"""
class company():
    def __init__(self):
        self._companyname="google"          #access modifier - _ (protected variable)
                                             #can be accessed only within the class and child classes
    def companyname(self):
        print(self._companyname)
        
class b(company):
    pass

c1=company()
c1.companyname()
print(c1._companyname)
c2=b()
c2.companyname()
"""









































































































