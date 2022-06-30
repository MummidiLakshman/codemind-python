def prime(a):
    if(a==1):
        return 0
    for i in range(2,(a//2)+1):
        if(a%i==0):
            return 0
    else:
        return 1
a=int(input())
b=list(map(int,input().split()))
c=0
s=0
for i in b:
    if(prime(i)):
        s+=i
        c+=1
d=s/c
print("%.2f"%d)