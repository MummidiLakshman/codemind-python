def prime(a):
    if(a==1):
        return 0
    for i in range(2,(a//2)+1):
        if(a%i==0):
            return 0
    else:
        return 1
a=int(input())
for j in range(0,a):
    b=int(input())
    for j in range(1,b):
        if(prime(j)):
            s=j
    for j in range(b,b+100):
        if(prime(j)):
            f=j
            break
    if abs(b-s)<=abs(b-f):
        print(s)
    else:
        print(f)
        
    
    