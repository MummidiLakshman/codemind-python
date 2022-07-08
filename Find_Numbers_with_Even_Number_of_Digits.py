def rev(a):
    c=0
    while(a!=0):
        s=a%10
        a=a//10
        c+=1
    if(c%2==0):
        return 1
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))
d=0
for i in a:
    if(rev(i)):
        d+=1
print(d)

