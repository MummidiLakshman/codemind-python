n=int(input())
s=n*n
sum=0
while(s>0):
    a=s%10
    sum=sum+a
    s=s//10
if sum==n:
    print('Neon Number')
else:
    print('Not Neon Number')