def self(n):
    t=n
    d=len(str(n))
    c=0
    while(n!=0):
        s=n%10
        n=n//10
        if(s==0):
            continue
        if(t%s==0):
            c+=1
    if(d==c):
        return 1
    else:
        return 0
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(self(i)):
        print(i,end=' ')
