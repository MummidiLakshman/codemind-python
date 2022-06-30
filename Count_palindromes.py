def rev(a):
    c=0
    d=a
    while(a!=0):
        s=a%10
        c=c*10+s
        a=a//10
    if(c==d):
        return 1
    else:
        return 0
a=int(input())
b=list(map(int,input().split()))
c=0
for i in b:
    if(rev(i)):
        c+=1
print(c)
        