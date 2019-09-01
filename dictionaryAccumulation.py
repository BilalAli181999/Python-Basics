fd=open('file.txt','r')
data=fd.read()
dict={}
for c in data:
    if c not in dict:
        dict[c]=0
    else:
        dict[c]+=1    
    
#print(dict.items())


sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
last=[]
for i in range(len(sports)-3,len(sports)):
    last.append(i)

b = "My, what a lovely day"
x = b.split(',')
z = "".join(x)
y = z.split()
a = ",".join(y)
print(z)


sent = "Holidays can be a fun time when you have good company!"
phrase = sent
phrase = phrase + " Holidays can also be fun on your own!"

print(phrase)
print(sent)

a=10
print(id(a))
a+=1
print(id(a))


