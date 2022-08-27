n=input()
n=n.split()
k=[]
m=0
for i in n:
    s=len(i)
    k.append(s)
for i in k:
    if(i>m):
        m=i
print(m)