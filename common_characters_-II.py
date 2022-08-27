n=input()
n=n.lower()
m=input()
m=m.lower()
k=[]
p=[]
for i in n:
    if(i==' '):
        continue
    if i in m:
        k.append(i)
for j in m:
    if(i==' '):
        continue
    if j in n:
        k.append(j)
#print(k)
for i in k:
    if(i==' '):
        continue
    if i not in p:
        p.append(i)
#print(p)
s=len(p)
print(s)
