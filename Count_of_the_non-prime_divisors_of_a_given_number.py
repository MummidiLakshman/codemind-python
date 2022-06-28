a=int(input())
c=0
d=0
f=0
def prime(a):
    if(a==1):
        return 0
    for i in range(2,int(a**0.5)+1):
        if(a%i==0):
            return 0
    else:
        return 1
for j in range(1,a+1):
    if(a%j==0):
        s=j
        if(prime(s)):
            c+=1
        else:
            d+=1
    else:
        f+=1;
print(d)
    
