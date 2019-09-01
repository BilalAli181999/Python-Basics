data=[('Bilal','30','A'),('Hariss','09','B'),('Faraz','04','A-')]
fd=open('writeCsv.csv','w')
fd.write("Name,RollNo,Grade")
for i in data:
    fd.write('\n'+i[0]+','+i[1]+','+i[2])
