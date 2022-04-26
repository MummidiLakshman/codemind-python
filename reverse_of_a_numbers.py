n=int(input())
s=0
b=0
while(n>0):
    s=n%10
    b=b*10+s
    n=n//10
print(b)