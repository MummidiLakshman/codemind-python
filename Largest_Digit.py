n=int(input())
m=0
while(n>0):
    s=n%10
    if(m<s):
        m=s
    n=n//10
print(m)