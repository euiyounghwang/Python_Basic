
def make_twice(n):
    return n*2

f1 = make_twice
print(f1(3))


f2 = lambda n: n*2
print(f2(3))
print((lambda n: n*2)(3))



def proxy(f, data):
    print(f)
    print(f(data))

proxy(f1,7)
proxy(f2,7)
proxy((lambda n: n*2),7)


print('-'*50)
a = [1,2,23,44,5,26,7,89]
b = sorted(a)
print(b)
print(sorted(a, reverse=True))
a.sort()
print(a)


print('-'*50)
def even_first(n):
    return n%2

print(sorted(a, key=even_first))
print(sorted(a, key=lambda n:n%2))
print(sorted(a, key=lambda n:1-n%2))
print(sorted(a, key=lambda n:n%2, reverse=True))


print('-'*50)
colors = ['Yellow', 'green', 'RED', 'bLuE', 'WHITE']

print(sorted(colors))
print(sorted(colors, key=lambda s: s.lower()))
print(sorted(colors, key=lambda s: len(s)))

print('-'*50)
Options = [('RED',1), ('green',9), ('Blue',3),('YELLOW',8)]
print(sorted(Options))
print(sorted(Options, key=lambda t: t[1]))



# print(items)
# print(sorted(items))
# print(sorted(items, key=lambda t: t[1]))
#
# print(sorted(items, key=itemgetter(0)))
# print(sorted(items, key=itemgetter(1)))
# print(sorted(items, key=itemgetter(1, 0)))


print('-'*50)

def create_kma(filename):
    conn = sqllite3.con



