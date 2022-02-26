import json

t1 = '{"ip":"8.8.8.8."}'
print(t1)

j1 = json.loads(t1)
print(j1)
print(j1['ip'])


print('-'*50)
datetime = '''{
"time":"03:53:34",
"milimseconds":"223456",
"data" : "03-02"
}
'''

parsing = json.loads(datetime)
print(parsing)
print(parsing['time'])

print('-'*50)
for i in parsing:
    print(i, parsing[i])
