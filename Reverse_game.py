def rev(a):
    c=0
    while(a!=0):
        s=a%10
        c=c*10+s
        a=a//10
    return c
a=int(input())
b=list(map(int,input().split()))
for i in b:
    print(rev(i),end=' ')
        