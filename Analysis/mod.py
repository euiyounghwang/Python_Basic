def safe_sum(a, b):
   return a+b


def test_key(a):

    # 영한 : 영어 단어를 이용해서 한글 설명을 적어놓은 책
    # 영어 : key
    # 한글 : value

    # d = {'name': 'kim', 'age': 20}
    d = dict(name='kim', age=20)
    # print(d)
    # print(d['name'], d['age'])
    #
    # d['money'] = 100        # insert
    # print(d)
    #
    # d['money'] = 1000       # update
    # print(d)

    for k in d:
        print(k, d[k])

    print('*' * 50)
    print(d.items())
    #
    # for i in d.items():
    #     print(i, i[0], i[1])

    for k, v in d.items():
        print('---', k, v)

    a1, a2 = 3, 5
    e = {a1: 'hello', a2: 'python'}
    print(e)

    return 'success'