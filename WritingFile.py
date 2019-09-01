fd=open('writer.txt',"w")
for i in range(12):
    fd.write(str(i**i)+'\n')