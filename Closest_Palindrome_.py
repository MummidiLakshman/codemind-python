def pal(n):
    s=n
    f=0
    while(n!=0):
        d=n%10
        f=f*10+d
        n=n//10
    if(f==s):
        return 1
    else:
        return 0
a=int(input())
for i in range(a-1,0,-1):
    if(pal(i)):
        s=i
        break
for j in range(a+1,a+1000):
    if(pal(j)):
        d=j
        break
if abs(s-a)==abs(d-a):
    print(s,d,end=' ')
elif abs(s-a)<abs(d-a):
    print(s)
else:
    print(d)


    
        