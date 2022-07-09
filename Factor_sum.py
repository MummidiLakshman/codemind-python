def fac(a):
    s=0
    for i in range(1,a+1):
        if(a%i==0):
            s+=i
    return s
s=input()
d=[]
p=[]
c=0
#print(d)
for i in range(0,len(s)):
    if s[i]!=',':
        d.append(int(s[i]))
for i in range(0,len(d)):
    f=fac(d[i])
    if f in d:
        c=1
        p.append(d[i])
if(c==0):
    print('-1')
else:
    b=set(p)
    print(*b)

        
    