

def f_2(a=0, b=0, c=0):
    print(a,b,c)


f_2(4,5,6)
f_2(b=10)


print('-'*50)

def f_3(*args):
    # // *args unpacking
    print(args, *args)


f_3(10,11,12,13)
f_3(10)