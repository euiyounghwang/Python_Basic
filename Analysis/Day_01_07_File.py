# import this


def strFormat():
    a = '{:10.1f} {:10.5f}'.format(3.14, 3.1424)
    print(a)


def read_1(filename):
    f = open(filename, 'r')

    lines = f.readlines()
    print(*lines, sep='')
    # print(lines)

    # for line in lines:
    #     # print(line, end='')
    #     print(line.strip())

    f.close()

#
#
# def read_2(filename):
#     f = open(filename, 'r')
#
#    while True:
#        line = f.readline()
#        print(line)
#
#        if len(line) ==0:
#            break
#
#
#     f.close()


def read_3(filename):
    f = open(filename, 'r')

    for line in f:
        print(line.strip())

    f.close()


def read_4(filename):
    with open(filename, 'r') as f:

        for line in f:
            print(line.strip())

        # f.close()


def write():
    f = open('Data/zen_write.txt', 'w', encoding='utf-8')
    f.write('hello1\n')
    f.write('hello2\n')
    f.write('한글\n')
    f.close()


filename = 'Data/zen.txt'
read_1(filename)

write()

print('-'*50)



# So far I have learned that:
#
# *args = list of arguments -as positional arguments
# **kwargs = dictionary - whose keys become separate keyword arguments and the values become values of these arguments.

def f_4(**kwargs):
    print(kwargs)
    # print(**kwargs)


f_4(apple = 'fruit', cabbage = 'vegetable')
f_4(a=1,b=2,c=3)