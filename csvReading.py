fd=open("csv.csv",'r')
lines=fd.readline()
heading=lines.split(',')
print(heading[0],heading[1],heading[2])
data=fd.readlines()
for i in data:
  #  print(type(i))
    print(i.split(','))
