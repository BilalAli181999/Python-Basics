fd=open("file.txt","r")
data=fd.readlines(4)
for i in data:
   print(i)
fd.close()