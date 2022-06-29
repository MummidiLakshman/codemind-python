def rev(a):
    p=0
    f=a
    while(a!=0):
        s=a%10
        p=p*10+s
        a=a//10
    return p
a=int(input())
c=list(map(int,input().split()))
for i in c:
    print(rev(i),end=' ')