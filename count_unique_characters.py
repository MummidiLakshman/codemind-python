n=input()
n=n.lower()
c=0
for i in n:
    if(i==' '):
        continue
    if n.count(i)==1:
        c+=1
print(c)