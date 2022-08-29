n=input()
n=n.lower()
c=[]
d=''
for i in n:
    if(i==' '):
        continue
    if n.count(i)==1:
        c.append(i)
c.sort()
for i in c:
    d+=i
print(d)