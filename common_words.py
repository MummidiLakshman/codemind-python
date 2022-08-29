n=input()
n=n.lower()
m=input()
m=m.lower()
for i in m.split():
    for j in n.split():
        if(i==j):
            print(i,end=' ')
    
