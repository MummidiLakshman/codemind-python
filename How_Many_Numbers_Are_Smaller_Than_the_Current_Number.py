a=int(input())
b=list(map(int,input().split()))
for i in range(0,a):
    c=0
    for j in range(0,a):
        if(b[i]>b[j]):
            c+=1
    print(c,end=' ')
