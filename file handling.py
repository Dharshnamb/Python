
f=open("fruits.txt","w")
f.write("banana\n")
f.write("mango\n")
f.close()


f=open("fruits.txt","a")
f.write("apple\n")
f.write("orange\n")
f.close()

f=open("fruits.txt","r+")
con=f.readline()
print(con)
f.close()
