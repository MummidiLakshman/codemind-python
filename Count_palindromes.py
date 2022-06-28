def pal(a):
    f=a
    d=0
    while(a!=0):
        s=a%10
        d=d*10+s
        a=a//10
    if(f==d):
        return 1
    else:
        return 0
a=int(input())
b=list(map(int,input().split()))
c=0
for i in b:
    if(pal(i)):
        c+=1
print(c)