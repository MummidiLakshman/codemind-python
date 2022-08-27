n=input()
n=n.lower()
m=input()
m=m.lower()
k=[]
p=[]
for i in n:
    if(i==' '):
        continue
    if i not in m:
        k.append(i)
for j in m:
    if(i==' '):
        continue
    if j not in n:
        k.append(j)
for i in k:
    if i not in p:
        p.append(i)
s=len(p)
print(s)
