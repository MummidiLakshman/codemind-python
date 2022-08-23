n=int(input())
a=list(map(int,input().split()))
h=[]
for i in a:
    s=i*i
    h.append(s)
h.sort()
print(*h)
    