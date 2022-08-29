n=input().lower()
n=n.split()
m=input().lower()
m=m.split()
c=[]
d=0
for i in n:
    for j in m:
        if(i==j):
            d+=1
            c.append(i)
print(d)