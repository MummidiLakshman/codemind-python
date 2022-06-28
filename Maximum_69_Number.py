n=int(input())
c=0
r=0
h=0
while(n!=0):
    s=n%10
    r=r*10+s
    n=n//10
while(r!=0):
    f=r%10
    if(f==6 and c==0):
        f=9
        c+=1
    h=h*10+f
    r=r//10
print(h)
