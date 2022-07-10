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
a=int(input())
b=list(map(int,input().split()))
for i in range(0,a):
    print(rev(b[i]),end=' ')
