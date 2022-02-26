
a = [1,3,5,7,9,0,2,4,6,8]


# print(a[::-1])
# print(a[len(a)-1:0:-1])
# print(a[len(a)-1:-1:-1])
# print(a[-1:-1:-1])
# print(a[3:3])
# print(a[::-2])
# print(a[-2::-2])
# print('-'*50)

# for i in range(0, len(a), 2):
# a 리스트 앞쪽 절반만 출력
# for i in range(0, len(a)//2):
#     print(a[i], end=' ')
# print()
#
# print(a[:len(a)//2])

# 짝수번째 출력
# for i in range(len(a)//2, len(a)):
#     print(a[i], end=' ')


# 거꾸로 출력
for i in reversed(a):
    print(i, sep=',')

print('-'*50)

for i in range(len(a)-1, -1, -1):
    print(a[i], end=' ')


print('\n')
print('-'*50)
c = a.copy()
print(c)

print('\n\n')
print('-'*50)
#
# try:
#     a = input('input....')
#     print(int(a))
# except ValueError:
#     print('ValueErro

try:
    a = [3, 5, 7]
    print(a[len(a)])
except IndexError:
    print('ValueError')



def returnInteger(a):
    return a;

try:
    a = input('input....')
    print(returnInteger(a))
except IndexError:
    print('ValueError')




