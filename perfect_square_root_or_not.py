n=int(input())
s=0
for i in range(1,n+1):
    if(i*i==n):
        print('True')
        break
else:
    print('False')