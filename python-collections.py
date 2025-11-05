#LISTS - CAN BE MODIFIED
"""
a=[1,2,3,4,5]
b=[7,8,9,10]
print(type(a))               #print datatype
print(a) 
a.append(6)                  #add another number
a.append(True)               #add boolean value
a.append("emc")              #add string value
print(a)
a.insert(4,"hi")             #insert a value in a position
print(a)
print(a[1])                  #print a element in a specific position
a[1]=11                      #modify an element in a specific position
print(a)
a.pop()                      #remove last element
print(a)
a.pop(3)                     #remove an element from a specific position
print(a)
a.extend(b)                  #join two list
print(a)
"""
#TUPLE - CANNOT BE MODIFIED
"""
a=(1,2,3,4,5)
c=[7,8,9,10]
print(a)
print(type(a))              #print datatype
b=list(a)                   #casting from tuple to list
print(b)
print(type(b))               #print datatype
b.append(6)                  #add another number
b.append(True)               #add boolean value
b.append("emc")              #add string value
print(b)
b.insert(4,"hi")             #insert a value in a position
print(b)
print(b[1])                  #print a element in a specific position
b[1]=11                      #modify an element in a specific position
print(b)
b.pop()                      #remove last element
print(b)
b.pop(3)                     #remove an element from a specific position
print(b)
b.extend(c)                  #join two list
print(b)
"""
#SET - CANNOT HAVE DUPLICATE, CANNOT MODIFY BUT ADD OR REMOVE IN SETS,UNORDERED,COLLECTION OF ALL DATATYPES
"""
a={1,2,3,4,1,(1,2),[1,2]}
print(a)
print(type(a))              #print datatype
a.add(10)                   #add an element
print(a)
a.remove(3)                 #remove an element
print(a)
a.pop()                     #pop an element
print(a)
"""
#DICTIONARY - KEY VALUE PAIR, COLLECTION OF ALL DATATYPES
"""
a={
    "name":"emc",
    "age":20,
    "location":"erode",
    "course":["python","sql"] 
    }
print(type(a))              #print datatype
a["color"]="red"            #adding an elemnt
print(a)
print(a["name"])            #print a specific element
print(a["course"])
a.pop("age")
del a["location"]           #remove an element
print(a)
"""



































































