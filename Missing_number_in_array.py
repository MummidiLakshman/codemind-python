n=int(input())
for i in range(0,n):
    a=int(input())
    k=list(map(int,input().split()))
    i=k[0]
    while(1):
        if i not in k:
            print(i)
            break
        i+=1