n=input().lower()
n=n.split()
m=input().lower()
m=m.split()
c=0
s=[]
k=[]
h=''
for i in n:
    if n.count(i)==1:
        s.append(i)
for i in m:
    if m.count(i)==1:
        k.append(i)
for i in s:
    for j in k:
        if(i==j):
            c+=1
print(c)
    
    