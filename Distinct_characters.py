n=input()
n=n.lower()
s=[]
k=''
for i in n:
    if(i==' '):
        continue
    if n.count(i)==1:
        s.append(i)
s.sort()
for i in s:
    k+=i
print(k)