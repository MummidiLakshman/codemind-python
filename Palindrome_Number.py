def pal(a):
    s=a
    f=0
    while(a>0):
        g=a%10
        f=f*10+g
        a=a//10
    if(f==s):
        return 1
    else:
        return 0
a=int(input())
for i in range(0,a):
    d=int(input())
    if(pal(d)):
        print('True')
    else:
        print('False')
        