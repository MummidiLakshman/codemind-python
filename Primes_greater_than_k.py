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
k=int(input())
c=0
for i in b:
    if(prime(i)):
        if(i>=k):
            c+=1
print(c)