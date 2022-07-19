n=int(input())
for i in range(0,n):
    s=input()
    for i in s:
        if i.isdigit():
            print('Yes')
            break
    else:
        print('No')