def sq(a):
    for i in range(1,a):
        if(i*i==a):
            return True
            break
    else:
        return False
a=int(input())
for i in range(0,a):
    c=int(input())
    if(sq(c)):
        print('True')
    else:
        print('False')
        
            