ages = {'si1wa': [['1','2','3']], 'sunshine': [['11','22','33']], 'tom': [['5','2','3'],['4'],['66666']]}
for key in ages.keys():  # keys() 생략 가능
    print(key)


for key, value in ages.items():
    print('{}의 나이는 {}입니다'.format(key, value[0]))
    for item in value:
        print(key, '!!! >> ', item)

print('*'*50)
print(ages['tom'])
print(ages['tom'][0])
print(ages['tom'][1])
print('\n')
print('*'*50)
for item in ages['tom']:
    print(item)