def prime(n):
    if(n==1):
        return 0
    for i in range(2,(n//2)+1):
        if(n%i==0):
            return 0
    return 1
n=int(input())
c=0
d=0
if(prime(n)):
    while(n>0):
        s=n%10
        n=n//10
        c+=1
        if(prime(s)==1):
            d+=1
    if(d==c):
        print('Mega Prime')
    else:
        print('Not Mega Prime')
else:
    print('Not Mega Prime')