a=int(input())
c=0
d=0
def prime(a):
    if(a==1):
        return 0
    for i in range(2,(a//2)+1):
        if(a%i==0):
            return 0
    else:
        return 1
if(prime(a)):
    while(a>0):
        s=a%10
        a=a//10
        c+=1
        if(prime(s)):
            d+=1
    if(c==d):
        print('Mega Prime')
    else:
        print('Not Mega Prime')
else:
    print('Not Mega Prime')
            
            
            
            