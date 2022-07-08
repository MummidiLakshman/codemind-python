n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if a.count(i)==1:
            c=1
            print(i,end=' ')
if(c==0):
    print('-1')