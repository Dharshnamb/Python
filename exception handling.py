#COMPILE TIME ERROR
"""
print("hi")
print("bye")
prinnt("hey")                #compile time error - name error - syntaxerror
"""
#LOGICAL ERROR
"""
a=10
b=20
print(a+a)                   #logical error - semantic error
"""
#RUNTIME ERROR
"""
a=int(input("enter a:"))
b=int(input("enter b:"))     #if enter str for input of b - runtime error - value error
print(a+b)
"""
#HANDLING EXCEPTION
"""
try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))     
    print(a+b)
except Exception as e:
    print("something",e)
"""
"""
try:
    a=input("enter a:")
    b=input("enter b:")    
    print(a/b)
except Exception as e:
    print("something",e)
"""
"""
try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    c=input("enter c:")
    print(c/b)
    print(d)
except ValueError as e:
    print("Value Error", e)
except TypeError as e:
    print("Type Error",e)
"""
"""
try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    c=input("enter c:")
    print(d)
except ValueError as e:
    print("Value Error", e)
except TypeError as e:
    print("Type Error",e)
except Exception as e:
    print("Something wrong",e)
"""
"""
try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    c=input("enter c:")
except ValueError as e:
    print("Value Error", e)
except TypeError as e:
    print("Type Error",e)
finally:
    print("Done")
"""

































    
