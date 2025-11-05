"""
for i in "APPLE":
    print(i)
"""
"""
for i in range(21):
    print(i)
"""
"""
for i in range(1,5):
    print(i)
"""
"""
for i in range(1,11):
    print(i,"x 2 =",1*2)             #2 table
"""
"""
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
for i in range(a+1,b):
      print(i)
"""
"""
for i in range(1,11):                #even number 1 to 10
    if(i%2==0):
        print(i)
"""
"""
n=0
for i in range(1,11):               #count of even numbers 1 to 10
    if(i%2):
        n=n+1
print(n)
"""
"""
odd=0
even=0
for i in range(1,11):               #count odd and even numbers 1 to 10
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print("Even:",even)
print("Odd:",odd)
"""
"""
count=0
for i in range(1,101):              #count of numbers 1 to 100 divisible by 3 and 5
    if(i%3==0 and i%5==0):
        count=count+1
print(count)
"""
#FOR LOOP WITH LISTS
"""
sum=0
for i in range(1,6):                #sum of first 5 natural numbers
    sum=sum+i
print(sum)
"""
"""
sum=0
a=[]
for i in range (5):
    num=int(input("Enter number"+str(i+1)+":")) #sum of numbers input by user
    a.append(num)
    sum=sum+num
print("LIST:",a)
print("SUM:",sum)
avg=sum/10
print("AVERAGE:",avg)
"""
"""
sum=0                                           #sum of first n natural numbers  
a=[]                                           
n=int(input("Enter the no.of natural numbers:"))
for i in range(1,n+1):
    a.append(i)
print("The first "+str(n)+" natural numbers are:",a)
for i in a:
    sum=sum+i
print(sum)
"""
"""
num=int(input("Input number of terms:"))       #cube of first n integers
for i in range(1,num+1):
    print("Number is: "+str(i)+" and cube of "+str(i)+" is:",i*i*i)
"""
#NESTED FOR LOOP
"""
for i in range(1,6):
    for j in range(1,3):
        print(i,j,"APPLE")
"""
"""
for i in range(1,4):
    print("WEEK: "+str(i))
    for j in range(1,4):
        print("DAY "+str(j))
    print("--------------")
print("------------------")
"""

for i in range(5):
    print( )
    for j in range(i):
        print("*",end="")
        
























































