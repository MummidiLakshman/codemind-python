def prime(a):
    if(a==1):
        return False 
    for i in range(2,(a//2)+1):
        if(a%i==0):
            return False
    else:
        return True
a=int(input())
b=list(map(int,input().split()))
c=0
for i in b:
    if(prime(i)):
        c+=1
print(c)