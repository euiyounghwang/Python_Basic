

class Info:
    def __init__(self, name):
        print('c-tor')
        self.name = name;

    def show(self):
        print('show')
        # print('show', self.age)

    def __str__(self):
        return '<Base> : {}'.format(self.name)


# Info.show(1)     # Unbound Method
# a, b = Info('kim'), Info('hwang')
# print(a.__str__())

# Info.show(a)
# a.show()
# b.show()


class Detail(Info):
    def __init__(self):
        Info.__init__(self, 'han')
        print(Info.__str__(self))

    @staticmethod
    def whatsup():
        print('aha...')

d1 = Detail()
d1.show()
Detail.whatsup()



class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print('*'*50)
print('cal1')
print(cal1.adder(3))
print(cal1.adder(4))
print(cal1.adder(4))
print('cal2')
print(cal2.adder(3))
print(cal2.adder(7))