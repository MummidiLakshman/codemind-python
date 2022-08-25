n=input()
n=n.lower()
s=[]
k=''
for i in n:
    if(i==' '):
        continue
    if i not in s:
        s.append(i)
s.sort()
for i in s:
    k+=i
print(k)