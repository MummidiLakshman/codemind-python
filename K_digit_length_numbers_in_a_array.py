def rev(a):
    c=0
    if(a<0):
        a=a*(-1)
    elif(a==0):
        c+=1
    while(a!=0):
        s=a%10
        a=a//10
        c+=1
    return c
a,b=map(int,input().split())
c=list(map(int,input().split()))
d=0
for i in range(0,a):
    if(rev(c[i])==b):
        d+=1
print(d)