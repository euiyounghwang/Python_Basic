import re

# db = '''1
# 2
# 3'''

db = '''3412    Bob[[ 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  tlice 535
1548  Kerry 534'''

ns = re.findall(r'[0-9]+',db)
print(ns)

# names = re.findall(r'[A-z]+',db)
names = re.findall(r'[A-Z][a-z]+',db)
print(names)

print('-'*100)
p = re.compile('[a-z]+')
m = p.match("tony")
print('*'*50,m)

print('-'*100)

print(re.findall(r'[a-z]+',db))
print('XXXXXXXXXXXXX'*100)
print(re.findall(r'[T][a-z]+',db,re.IGNORECASE))
# print(re.findall(r'[A-SU-Z][a-z]+',db))
print('-'*100)
print(re.findall(r'P[a-z]+',db))
print(re.findall(r'K[a-z]+',db))



print('-'*100)
print(re.findall(r'[0-9][0-9][0-9][0-9]',db))
print(re.findall(r'^[0-9]+',db, re.MULTILINE))
print('-'*100)
print(re.findall(r'[0-9]+$',db, re.MULTILINE))