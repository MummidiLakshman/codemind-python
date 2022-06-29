def rev(a):
    c=0
    while(a!=0):
        s=a%10
        a=a//10
        c+=1
    return c
a=int(input())
b=list(map(int,input().split()))
s=min(b)
p=rev(s)
d=0
for i in b:
    if(rev(i)==p):
        d+=1
print(d)