def square(a):
    for i in range(1,a+1):
        if(i*i==a):
            print('True')
            return 0
    print('False')
a=int(input())
square(a)