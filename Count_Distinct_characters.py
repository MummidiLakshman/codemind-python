n=input()
n=n.lower()
c=[]
d=0
for i in n:
    if(i==' '):
        continue
    if i not in c:
        c.append(i)
        d+=1
print(d)
