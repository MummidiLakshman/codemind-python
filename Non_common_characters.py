n=input()
n=n.lower()
m=input()
m=m.lower()
c=[]
p=[]
h=''
o=0
for i in n:
    if(i==' '):
        continue
    if i not in m:
        c.append(i)
for i in m:
    if(i==' '):
        continue
    if i not in n:
        c.append(i)
for i in c:
    if i not in p:
        p.append(i)
        o+=1
p.sort()
print(o)
    