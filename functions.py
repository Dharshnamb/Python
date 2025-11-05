"""
def painter():
    print("Painting")
painter()
"""
"""
def add():
    a=int(input("a="))
    b=int(input("b="))                                 #different arithmetic operations
    print("a+b=",a+b)
def sub():
    a=int(input("a="))
    b=int(input("b="))
    print("a-b=",a-b)
def mul():
    a=int(input("a="))
    b=int(input("b="))
    print("axb=",a*b)
def div():
    a=int(input("a="))
    b=int(input("b="))
    print("a/b=",a/b)

add()
sub()
mul()
div()
"""
"""
def painter(msg):
    print("The msg is:",msg)                        #using parameters and arguments

painter("Paint my house")
"""
"""
def findevenorodd(num):                            #finding even or odd
    if(num%2==0):
        print("Even")
    else:
        print("Odd")

num=int(input("Enter a number:"))
findevenorodd(num)
"""
"""
def findpassorfail(mark):
    if(mark<35):                                #finding pass or even
        print("Fail")
    else:
        print("Pass")
score=int(input("Enter your mark:"))
findpassorfail(score)
"""
"""
def printrange(a,b):
    for i in range(a,b+1):                      #printing range
        print(i)

a=int(input("Enter small number:"))
b=int(input("Enter bigger number:"))
printrange(a,b)
"""
#RETURN KEYWORD IN PYTHON
"""
def painter():
    return "I am painter"

print(painter())
"""
"""
s_username="emc"
s_password="123"

username=input("username:")
password=input("password:")                    #checking username and password 

def validate():
    if(s_username==username and s_password==password):
        return "Correct"
    else:
        return "Wrong"

print(validate())
"""
"""
a=int(input("Enter a:"))                       #adding with return func and multiplying
b=int(input("Enter b:"))
c=int(input("Enter c:"))
def add():
    return a+b

final=add()*c
print(final)
"""



















































































