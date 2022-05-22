n=int(input())
def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
a=[]
for i in range(0,n):
    b=int(input())
    a.append(b)
    print(fact(a[i]))
    