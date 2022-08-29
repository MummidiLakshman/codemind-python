n=input()
v='aeiouAEIOU'
s=[]
c=0
p=[]
for i in n:
    if i in v:
        s.append(i)
for i in s:
    if i not in p:
        p.append(i)
        c+=1
#print(*p)
if(c==0):
    print('-1')
else:
    print(*p)