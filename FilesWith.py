with open('file.txt','r') as fd:
    data=fd.read()
    #print(data)
    print(data.split('\n'))