n=int(input())
s=0
for i in range(1,n+1//2):
    if(n%i==0):
        s=s+i
if(s!=n):
    print('False')
else:
    print('True')

    