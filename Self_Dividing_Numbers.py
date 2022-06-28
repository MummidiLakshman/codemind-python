def selff(n):
    d=len(str(n))
    t=n
    v=0
    while(n!=0):
        s=n%10
        n=n//10
        if(s==0):
            continue
        else:
            if(t%s==0):
                v+=1
    if(v==d):
        return 1
    else:
        return 0
a=int(input())
j=int(input())
for i in range(a,j+1):
    if(selff(i)):
        print(i,end=' ')