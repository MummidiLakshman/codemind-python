n=input().split(" ")
d=min(n[len(n)-1])
#print(d)
if d==d.lower():
    print(d)
else:
    h=d.lower()
    if h in n[len(n)-1]:
        print(h)
    else:
        print(d)
        
    