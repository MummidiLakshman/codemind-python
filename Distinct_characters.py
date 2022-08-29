n=input()
n=n.lower()
c=[]
d=''
for i in n:
    if(i==' '):
        continue
    if i not in c:
        c.append(i)
c.sort()
for i in c:
    d+=i
print(d)
