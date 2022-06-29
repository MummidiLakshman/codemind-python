def rev(a):
    c=0
    while(a!=0):
        s=a%10
        a=a//10
        c+=1
    return c
a=int(input())
c=list(map(int,input().split()))
d=0
f=min(c)
p=rev(f)
for i in c:
    if(rev(i)==p):
        d+=1
print(d)