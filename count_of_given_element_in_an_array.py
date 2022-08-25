n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=0
for i in a:
    if(i==b):
        c+=1
if(c==0):
    print('0')
else:
    print(c)