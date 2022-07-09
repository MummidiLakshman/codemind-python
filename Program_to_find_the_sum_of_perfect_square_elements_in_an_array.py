def sq(a):
    for i in range(1,a+1):
        if(i*i==a):
            return 1
    return 0
a=int(input())
b=list(map(int,input().split()))
d=0
for i in range(0,a):
    if(sq(b[i])):
        d+=b[i]
print(d)
        
    