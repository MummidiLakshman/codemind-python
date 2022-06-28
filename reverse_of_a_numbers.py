n=int(input())
d=0
while(n!=0):
    s=n%10
    d=d*10+s
    n=n//10
print(d)