def dig(n):
    f=0
    while(n!=0):
        s=n%10
        f+=s
        n=n//10
    return f
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    c+=dig(i)
print(c)
