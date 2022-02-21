
**Add 클래스에서 두 개의 수를 받아 덧셈을 하는 add 함수를 구현해주세요.**  
```sh
class Add: 
    def add(self, n1, n2):
        return n1+n2
```        

**#2 Calculator 클래스가 Add 클래스를 상속받도록 하세요.**  
```sh
class Calculator(Add):
    def sub(self, n1, n2):
        return n1 - n2
```

```sh
obj = Calculator()
print(obj.sub(1,2))
#3 obj 객체를 사용하여, 정수 1과 2를 더하는 연산을 해보세요. 
print(obj.add(1,2))

** -1 **  
** 3 **  
코드 실행이 완료되었습니다
```



**1. 실행 버튼을 눌러 출력되는 오류 메시지를 확인해보세요.**  
```sh
try:
    print(param)
except Exception as e:
    print(e)


name 'param' is not defined
코드 실행이 완료되었습니다.
```


**1. try~except~else문을 실행해보세요.**  
```sh
try:
    print('안녕하세요.')
    # 2. print(param)을 주석 처리한 후 실행・제출해보세요.
    #print(param)
except:
    print('예외가 발생했습니다!')
else:
    print('예외가 발생하지 않았습니다.')


안녕하세요.
예외가 발생하지 않았습니다.
코드 실행이 완료되었습니다.
```

```sh
**1. 실행버튼을 클릭한 후 터미널에 '안녕하세요 파이썬'을 입력해보세요.**  
k = input('<값>을 입력하세요: ')

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print('당신이 입력한 값은 <' + k + '>입니다.')

<값>을 입력하세요: 안녕하세요 파이썬
당신이 입력한 값은 <안녕하세요 파이썬>입니다.

```

```sh
# 실습에 사용될 변수를 선언합니다. 수정하지 마세요.
a = 11113
b = 23

# 실습에 사용될 변수를 선언합니다. 수정하지 마세요.
m = 12400
h = 60

# 1. a를 b로 나누었을 때의 몫과 나머지 값을 각각 ret1, ret2에 저장하세요.
ret1, ret2 = divmod(a,b)

# 2. m을 h로 나누었을 때의 몫과 나머지 값을 각각 ret3, ret4에 저장하세요.
ret3, ret4 = divmod(m,h)

# 실습 결과를 출력하는 코드입니다. 수정하지 마세요. 
print('<%d/%d>는 몫이 <%d>, 나머지가 <%d>입니다.' %(a, b, ret1, ret2))
print('<%d>분은 <%d시간 %d분>으로 변환할 수 있습니다.' %(m, ret3, ret4))

<11113/23>는 몫이 <483>, 나머지가 <4>입니다.
<12400>분은 <206시간 40분>으로 변환할 수 있습니다.

```

```sh
# 1. 97을 16진수로 변환한 후 h1에 저장하세요.
h1 = hex(97)

# 2. 98을 16진수로 변환한 후 h2에 저장하세요.
h2 = hex(98)

# 3. h1에 저장된 값을 10진수로 변환한 후 a에 저장하세요.
a = int(h1,16)

# 4. h2에 저장된 값을 10진수로 변환한 후 b에 저장하세요.
b =  int(h2,16)

# 5. a와 b를 더한 값을 16진수로 변환한 후 ret에 저장하세요.
ret =  hex(a+b)

# 실습 결과를 출력하는 코드입니다. 수정하지 마세요. 
print(h1)
print(h2)
print(a)
print(b)
print(ret)

0x61
0x62
97
98
0xc3
```


```sh
# 1. 97을 2진수로 변환한 후 b1에 저장하세요.
b1 = bin(97)

# 2. 98을 2진수로 변환한 후 b2에 저장하세요.
b2 = bin(98)

# 3. b1에 저장된 값을 10진수로 변환한 후 a에 저장하세요.
a = int(b1, 2)

# 4. b2에 저장된 값을 10진수로 변환한 후 b에 저장하세요.
b = int(b2, 2)

# 5. a와 b를 더한 값을 2진수로 변환한 후 ret에 저장하세요.
ret = bin(a+b)

# 실습 결과를 출력하는 코드입니다. 수정하지 마세요. 
print(b1)
print(b2)
print(a)
print(b)
print(ret)


0b1100001
0b1100010
97
98
0b11000011
```


```sh
# 1. 정수 -3의 절대값을 abs1에 저장하세요.
abs1 = abs(-3)

# 2. 실수 -5.72의 절대값을 abs2에 저장하세요.
abs2 = abs(-5.72)

# 3. 복소수 3+4j의 절대값을 abs3에 저장하세요.
abs3 = abs(3+4j)

# 실습 결과를 출력하는 코드입니다. 수정하지 마세요. 
print(abs1)
print(abs2)
print(abs3)

3
5.72
5.0
```


```sh
# 1. 정수 1118을 소수점 첫째자리에서 반올림한 값을 ret1에 저장하세요.
ret1 = round(1118,0)

# 2. 실수 16.554를 소수점 첫째자리에서 반올림한 값을 ret2에 저장하세요.
ret2 = round(16.554,0)

# 3. 정수 1118를 1의자리에서 반올림한 값을 ret3에 저장하세요.
ret3 =  round(1118,-1)

# 4. 실수 16.554를 소수점 셋째자리에서 반올림한 값을 ret4에 저장하세요.
ret4 =  round(16.554,2)

# 실습 결과를 출력하는 코드입니다. 수정하지 마세요. 
print(ret1)
print(ret2)
print(ret3)
print(ret4)

1118
17.0
1120
16.55
```


```sh
# 실습에 사용될 변수를 선언합니다. 수정하지 마세요.
listdata = [9.96, 1.27, 5.07, 6.45, 8.38, 9.29, 4.93, 7.73, 3.71, 0.93]
txt = 'Alotofthingsoccureachday'

# 1. listdata의 최대값을 maxlist에 저장하세요.
maxlist = max(listdata)

# 2. listdata의 최소값을 minlist에 저장하세요.
minlist = min(listdata)

# 3. txt의 최대값을 maxtxt에 저장하세요.
maxtxt = max(txt)

# 4. txt의 최소값을 mintxt에 저장하세요.
mintxt = min(txt)

# 5. 2+3, 2*3, 2**3, 3**2 중 최대값을 maxval에 저장하세요.
maxval = max([2+3, 2*3, 2**3, 3**2 ])

# 6. 'abz', 'a12'의 최소값을 minval에 저장하세요.
minval = min(['abz', 'a12'])

# 실습 결과를 출력하는 코드입니다. 수정하지 마세요. 
print(maxlist)
print(minlist)
print(maxtxt)
print(mintxt)
print(maxval)
print(minval)

9.96
0.93
y
A
9
a12
```

```sh
# 실습에 사용할 변수를 선언합니다. 수정하지 마세요.
txt = 'abcdefghijk'

# 1. txt에 저장된 문자열을 거꾸로 만들어 변수 ret에 저장하세요.
ret = txt[::-1]

# 실습 결과를 출력하는 코드입니다. 수정하지 마세요. 
print(ret)
kjihgfedcba
```


```sh
# 실습에 사용할 변수를 선언합니다.
word = 'Python'
sentence = '파이썬은 1991년 프로그래머 귀도 반 로섬이 발표한 고급 프로그래밍 언어이다.'
paragraph = 'Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy that emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly brackets or keywords), and a syntax that allows programmers to express concepts in fewer lines of code than might be used in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale.'

# 1. 변수 `word`에 저장된 문자열의 길이를 구하고, `word_len` 변수에 저장하세요.
word_len = len(word)

# 2. 변수 `sentence`에 저장된 문자열의 길이를 구하고, `sentence_len` 변수에 저장하세요. 
sentence_len = len(sentence)

# 3. 변수 `paragraph`에 저장된 문자열의 길이를 구하고, `paragraph_len` 변수에 저장하세요.
paragraph_len =  len(paragraph)

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print('word에 저장된 단어는 %d개의 문자로 이루어져있습니다.' %word_len) 
print('sentence에 저장된 문장은 %d개의 문자로 이루어져있습니다.' %sentence_len) 
print('paragraph에 저장된 문단은 %d개의 문자로 이루어져있습니다.' %paragraph_len) 

word에 저장된 단어는 6개의 문자로 이루어져있습니다.
sentence에 저장된 문장은 44개의 문자로 이루어져있습니다.
paragraph에 저장된 문단은 576개의 문자로 이루어져있습니다.
```

```sh
# 실습에 사용할 변수를 선언합니다.
txt1 = 'A'
txt2 = '안녕'
txt3 = 'Warcraft Three'
txt4 = '3PO'

# 1. txt1이 알파벳/한글로만 구성되었는지 확인하고 그 결괏값을 변수 ret1에 저장하세요.
ret1 = txt1.isalpha()

# 2. txt2가 알파벳/한글로만 구성되었는지 확인하고 그 결괏값을 변수 ret2에 저장하세요.
ret2 = txt2.isalpha()

# 3. txt3이 알파벳/한글로만 구성되었는지 확인하고 그 결괏값을 변수 ret3에 저장하세요.
ret3 =txt3.isalpha()

# 4. txt4이 알파벳/한글로만 구성되었는지 확인하고 그 결괏값을 변수 ret4에 저장하세요.
ret4 =txt4.isalpha()

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(ret1)
print(ret2)
print(ret3)
print(ret4)

True
True
False
False
```


```sh
# 실습에 사용할 변수를 선언합니다.
txt1 = '010-1234-5678'
txt2 = '010 1234 5678'
txt3 = 'R2D2'
txt4 = '0125'

# 1. txt1이 숫자로 구성되었는지 확인하고 그 결괏값을 변수 ret1에 저장하세요.
ret1 = txt1.isdigit()

# 2. txt2이 숫자로 구성되었는지 확인하고 그 결괏값을 변수 ret2에 저장하세요.
ret2 = txt2.isdigit()

# 3. txt3이 숫자로 구성되었는지 확인하고 그 결괏값을 변수 ret3에 저장하세요.
ret3 = txt3.isdigit()

# 4. txt4이 숫자로 구성되었는지 확인하고 그 결괏값을 변수 ret4에 저장하세요.
ret4 = txt4.isdigit()

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(ret1)
print(ret2)
print(ret3)
```

```sh
# 실습에 사용할 변수를 선언합니다.
num1 = 1234
num2 = 3.14

# 1. 수치형 자료 num1를 문자열로 변환한 값을 numstr1에 저장하세요.
numstr1 = str(num1)

# 2. 수치형 자료 num2를 문자열로 변환한 값을 numstr2에 저장하세요.
numstr2 = str(num2)

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print('num1을 문자열로 변환한 값은 "%s"입니다.' %numstr1)
print('num2을 문자열로 변환한 값은 "%s"입니다.' %numstr2)

num1을 문자열로 변환한 값은 "1234"입니다.
num2을 문자열로 변환한 값은 "3.14"입니다.
print(ret4)

False
False
False
True
```

```sh
# 실습에 사용할 변수를 선언합니다.
txt1 = '안녕하세요?'
txt2 = '1. Title-제목을 넣으세요'
txt3 = '3피오R2D2'

# 1. txt1이 알파벳/한글/숫자로 구성되었는지 확인하고 그 결괏값을 변수 ret1에 저장하세요.
ret1 = txt1.isalnum()

# 2. txt2이 알파벳/한글/숫자로 구성되었는지 확인하고 그 결괏값을 변수 ret2에 저장하세요.
ret2 = txt2.isalnum()

# 3. txt3이 알파벳/한글/숫자로 구성되었는지 확인하고 그 결괏값을 변수 ret3에 저장하세요.
ret3 = txt3.isalnum()

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(ret1)
print(ret2)
print(ret3)

False
False
True
```


```sh
# 실습에 사용할 변수를 선언합니다.
txt = 'A lot of things occur each day, every day.'

# 1. txt 문자열에 'o'의 개수를 확인한 후 word_count1에 저장하세요.
word_count1 = txt.count('o')

# 2. txt 문자열에 'day'의 개수를 확인한 후 word_count2에 저장하세요.
word_count2 = txt.count('day')

# 3. txt 문자열에 공백(' ')의 개수를 확인한 후 word_count3에 저장하세요.
word_count3 = txt.count('.')

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(word_count1)
print(word_count2)
print(word_count3)

3
2
1
```

```sh
# 실습에 사용할 변수를 선언합니다.
txt = 'A lot of things occur each day, every day.'

# 1. 'e'가 최초로 나타는 위치의 인덱스를 offset에 저장하세요.
offset1 = txt.find('e')

# 2. 'day'가 최초로 나타는 위치의 인덱스를 offset에 저장하세요.
offset2 = txt.find('day')

# 3. 인덱스 30 이후에 'day'가 최초로 나타는 위치의 인덱스를 offset에 저장하세요.
offset3 = txt.find('day',30)

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(offset1)
print(offset2)
print(offset3)

22
27
38
```

```sh
# 실습에 사용할 변수를 선언합니다.
fb_url = 'https://www.facebook.com/elice.io'
blog_url = 'https://medium.com/elice'

# 1. 마침표(.)를 기준으로 fb_url에 저장된 문자열을 분리하세요.
ret1 = fb_url.split('.')

# 2. 슬래쉬(/)를 기준으로 blog_url에 저장된 문자열을 분리하세요.
ret2 = blog_url.split('/')

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(ret1)
print(ret2)


['https://www', 'facebook', 'com/elice', 'io']
['https:', '', 'medium.com', 'elice']
```

```sh
# 실습에 사용할 변수를 선언합니다.
strdata = 'pneumonoultramicroscopicsilicovolcanoconiosis'

# 1. `strdata`에 저장된 문자열을 오름차순으로 정렬해서 `ret1`에 저장하세요.
ret1 = sorted(strdata)

# 2. 리스트 형태의 `ret1`을 문자열로 결합하여 `ret1`에 다시 저장하세요.
ret1 = ''.join(ret1)

# 3. `strdata`에 저장된 문자열을 내림차순으로 정렬하여 `ret2`에 저장하세요.
ret2 = sorted(strdata, reverse=True)

# 4. 리스트 형태의 `ret2`을 문자열로 결합하여 `ret2`에 다시 저장하세요.
ret2 = ''.join(ret2)

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print('오름차순으로 정렬된 문자열은 <' + ret1 + '>입니다.')
print('내림차순으로 정렬된 문자열은 <' + ret2 + '>입니다.')

오름차순으로 정렬된 문자열은 <aacccccceiiiiiilllmmnnnnooooooooopprrsssstuuv>입니다.
내림차순으로 정렬된 문자열은 <vuutssssrrppooooooooonnnnmmllliiiiiieccccccaa>입니다.
```


```sh
# 안내문을 띄우고 엘리스 터미널에 입력한 사용자의 입력값을 ch에 저장합니다.
ch = input('문자를 1개를 입력하세요: ')
# try~except문을 실행합니다.
try:
    # 사용자가 입력한 문자의 코드값을 chv에 저장합니다. 
    chv = ord(ch)
    # 사용자가 입력한 문자와 문자의 코드값을 출력합니다.
    print('문자: %s \n코드값: %d' %(ch, chv))
# try 코드블럭에서 오류가 발생할 겨우 except에 해당하는 코드블럭을 실행합니다.
except:
    print('ERROR: ord()의 인자로 숫자 또는 한 개 이상의 문자를 입력할 경우 오류가 발생합니다!!!')


문자를 1개를 입력하세요: a
문자: a 
코드값: 97
```


```sh
# 실습에 사용할 변수를 선언합니다.
expr1 = '2+3'
expr2 = 'round(3.7)'

# 1. expr1에 저장된 문자열을 파이썬 코드로 실행하고 그 결과를 ret1에 저장하세요.
ret1 = eval(expr1)

# 2. expr2에 저장된 문자열을 파이썬 코드로 실행하고 그 결과를 ret2에 저장하세요.
ret2 = eval(expr2)

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(ret1)
print(ret2)

5
4
```

```sh
# 1. 0~9까지 순차적인 정수를 ret1에 저장하세요.
ret1 = range(10)

# 2. ret1에 저장된 0~9까지 순차적인 정수를 리스트 형태로 변환해 ret1_list에 저장하세요.
ret1_list = list(ret1)

# 3. 10~19까지 순차적인 정수를 ret2에 저장하세요.
ret2 =range(10,20)

# 4. ret2에 저장된 10~19까지 순차적인 정수를 리스트 형태로 변환해 ret2_list에 저장하세요.
ret2_list = list(ret2)

# 실습 결과를 출력하는 코드입니다. 수정하지 마세요. 
print(ret1_list)
print(ret2_list)

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```


```sh
# 실습에 활용할 변수를 선언합니다.
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕석', '해왕성']
earth = '지구'
saturn = '토성'

# 1. earth 변수를 사용해 solarsys 리스트에서 지구의 위치를 구하세요.
pos1 = solarsys.index(earth)

# 2. saturn 변수를 사용해 solarsys 리스트에서 토성의 위치를 구하세요. 
pos2 = solarsys.index(saturn)

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print('%s은(는) 태양계에서 %d번째에 위치하고 있습니다.' %(earth, pos1))
print('%s은(는) 태양계에서 %d번째에 위치하고 있습니다.' %(saturn, pos2))

지구은(는) 태양계에서 3번째에 위치하고 있습니다.
토성은(는) 태양계에서 6번째에 위치하고 있습니다.
```

```sh
# 실습에 활용할 변수를 선언합니다.
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']

# 1. solarsys의 인덱스1~4에 해당하는 멤버를 슬라이싱하여 만든 새로운 리스트를 rock_planets에 저장하세요.
rock_planets = solarsys[1:5]

# 2. solarsys의 인덱스5에 해당하는 멤버부터 끝까지 슬라이싱하여 만든 새로운 리스트를 gas_planets에 저장하세요.
gas_planets = solarsys[5:]

# 3. solarsys에서 `태양`을 제외하고 짝수 인덱스에 해당하는 멤버(수성, 지구, 목성, 천왕성)를 모두 슬라이싱하여 만든 새로운 리스트를 even_planets에 저장하세요. 
even_planets = solarsys[1:len(solarsys):2]

print('태양계의 암석형 행성: ', end = ''); print(rock_planets)
print('태양계의 가스형 행성: ', end = ''); print(gas_planets)
print('태양계의 짝수번째 행성: ', end = ''); print(even_planets)


태양계의 암석형 행성: ['수성', '금성', '지구', '화성']
태양계의 가스형 행성: ['목성', '토성', '천왕성', '해왕성']
태양계의 짝수번째 행성: ['수성', '지구', '목성', '천왕성']
```


```sh
# 실습에 사용할 변수를 선언합니다.
listdata1 = list(range(1,6))
listdata2 = list(range(10,16))

# 1. reverse()를 이용해 listdata1의 모든 요소 순서를 거꾸로 만드세요. 새로운 변수를 만들지 않고 원본 리스트를 변경하세요.
listdata1.reverse()

# 2. [::-1]를 이용해 listdata2의 모든 요소 순서를 거꾸로 만들고 ret에 저장하세요.
ret = sorted(listdata2[::-1], reverse=True)

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(listdata1)
print(ret)

[5, 4, 3, 2, 1]
[15, 14, 13, 12, 11, 10]
```


```sh
# 실습에 사용할 변수를 선언합니다.
solarsys = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']

# 1.index()를 이용해 solarsys에서 '화성'의 인덱스 값을 pos1에 저장하세요.
pos1 =  solarsys.index('화성')

# 2. solarsys에 '지구'와 '화성' 사이에 새로운 요소로 '달'을 삽입하세요. 
# pos1에 저장된 `화성`의 인덱스값을 사용하세요.
solarsys.insert(pos1, '달')

# 3. index()를 이용해 '달'이 추가된 solarsys에서 '천왕성'의 인덱스 값을 pos2에 저장하세요.
pos2 = solarsys.index('천왕성')

# 4. '달'이 추가된 solarsys에 '토성'과 '천왕성' 사이에 새로운 요소로 'B612'를 삽입하세요. 
# pos2에 저장된 `천왕성`의 인덱스값을 사용하세요.
solarsys.insert(pos2, 'B612')

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(solarsys)

['수성', '금성', '지구', '달', '화성', '목성', '토성', 'B612', '천왕성', '해왕성']
```

```sh
# 실습에 사용할 변수를 선언합니다.
solarsys = ['태양', '수성', '금성', '지구', '달', '화성', '목성', '토성', '천왕성', '해왕성']

# 1. remove를 이용해 solarsys 리스트에서 '태양'을 제거하세요. 
solarsys.remove('태양')

# 2. remove를 이용해 solarsys 리스트에서 '달'을 제거하세요.
solarsys.remove('달')

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(solarsys)

['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
```

```sh
# 실습에 사용할 변수를 선언합니다.
listdata = [2, 2, 1, 3, 8, 5, 7, 6, 3, 6, 2, 3, 9, 4, 4]
week = ['월', '화', '수', '목', '금', '금', '금']

# 1. listdata에서 값이 2인 요소 개수를 c1에 저장하세요
c1 = listdata.count(2)

# 2. listdata에서 값이 7인 요소 개수를 c2에 저장하세요
c2 =listdata.count(7)

# 3. week에서 값이 '토'인 요소 개수를 c3에 저장하세요
c3 = week.count('토')

# 4. week에서 값이 '금'인 요소 개수를 c4에 저장하세요
c4 = week.count('금')

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(c1)
print(c2)
print(c3)
print(c4)


3
1
0
3
```


```sh
# 실습에 사용할 변수를 선언합니다.
lotto770 = [34, 1, 43, 9, 12, 39, 23]
namelist = ['Marry', 'Sams', 'Aimy', 'Tom', 'Michael', 'Bob', 'Kelly']

# 1. sort를 이용해 lotto770의 원소를 오름차순으로 정렬하세요.
lotto770.sort()

# 2. sorted를 이용해 namelist의 원소를 알파벳 내림차순으로 정렬한 값을 ret에 저장하세요.
ret = sorted(namelist, reverse=True)

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(lotto770)
print(ret)


[1, 9, 12, 23, 34, 39, 43]
['Tom', 'Sams', 'Michael', 'Marry', 'Kelly', 'Bob', 'Aimy']
```

```sh
# 실습에 사용할 random 모듈의 shuffle을 임포트합니다.
from random import shuffle

# 실습에 사용할 변수를 선언합니다.
listdata = list(range(1, 11))

# 1. listdata를 무작위로 섞어보세요. 8번째 줄에 코드를 작성하세요. print문은 수정하지마세요.
shuffle(listdata)
print(listdata)

# 2. listdata를 다시 무작위로 섞어보세요. 12번째 줄에 코드를 작성하세요. print문은 수정하지마세요.
shuffle(listdata)
print(listdata)

# 3. listdata를 한 번 더 섞어보세요. 16번째 줄에 코드를 작성하세요. print문은 수정하지마세요.
shuffle(listdata)
print(listdata)


[8, 2, 6, 10, 1, 3, 5, 9, 7, 4]
[5, 4, 9, 10, 7, 1, 8, 2, 6, 3]
[5, 6, 3, 7, 1, 2, 10, 4, 9, 8]
코드 실행이 완료되었습니다.
```


```sh
# 실습에 사용할 변수를 선언합니다.
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']

# 1. enumerate와 list를 이용해 solarsys의 모든 요소를 인덱스와 쌍으로 추출하여 ret에 저장하세요.
ret = list(enumerate(solarsys))

# 2. for문과 enumerate를 함께 사용한 아래 코드를 실행해보세요.
# solarsys의 인덱스와 요소를 각각 i와 body에 순서대로 저장합니다. 
for i, body in enumerate(solarsys):    
    # 첫번째 반복문에서는 태양의 인덱스0과 태양이 i와 body에 저장됩니다.
    print('태양계의 %d번째 천체: %s' %(i, body))

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(ret)


태양계의 0번째 천체: 태양
태양계의 1번째 천체: 수성
태양계의 2번째 천체: 금성
태양계의 3번째 천체: 지구
태양계의 4번째 천체: 화성
태양계의 5번째 천체: 목성
태양계의 6번째 천체: 토성
태양계의 7번째 천체: 천왕성
태양계의 8번째 천체: 해왕성
[(0, '태양'), (1, '수성'), (2, '금성'), (3, '지구'), (4, '화성'), (5, '목성'), (6, '토성'), (7, '천왕성'), (8, '해왕성')]
```


```sh
# 실습에 사용할 변수를 선언합니다.
listdata1 = [2, 2, 1, 3, 8, 5, 7, 6, 3, 6, 2, 3, 9, 4, 4]
listdata2 = list(range(103, 1226))

# 1. listdata1의 모든 요소의 합을 ret1에 저장하세요.
ret1 = sum(listdata1)

# 2. listdata2의 모든 요소의 합을 ret2에 저장하세요.
ret2 = sum(listdata2)

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(ret1)
print(ret2)


65
745672
```


```sh
### Composed by Yong Hee Lee ###

# 실습에 사용할 변수를 선언합니다.
listdata1 = [0, 1, 2, 3, 4]
listdata2 = [True, True, True]
listdata3 = ["", [], (), {}, None, False]

# 1. all()를 이용해 listdata1의 모든 요소가 참인지 또는 모든 요소가 거짓인지 확인하세요.
ret1 = all(listdata1)

# 2. any()를 이용해 listdata1의 모든 요소가 참인지 또는 모든 요소가 거짓인지 확인하세요.
ret2 = any(listdata1)

# 3. all()를 이용해 listdata2의 모든 요소가 참인지 또는 모든 요소가 거짓인지 확인하세요.
ret3 = all(listdata2)

# 4. any()를 이용해 listdata2의 모든 요소가 참인지 또는 모든 요소가 거짓인지 확인하세요.
ret4 = any(listdata2)

# 5. all()를 이용해 listdata3의 모든 요소가 참인지 또는 모든 요소가 거짓인지 확인하세요.
ret5 = all(listdata3)

# 6. any()를 이용해 listdata3의 모든 요소가 참인지 또는 모든 요소가 거짓인지 확인하세요.
ret6 = any(listdata3)

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(ret1)
print(ret2)
print(ret3)
print(ret4)
print(ret5)
print(ret6)


False
True
True
True
False
False
```


```sh
# 실습에 사용할 변수를 선언합니다.
solardict = {}

# 1. solardict에 키가 '태양', 값이 'Sun'인 요소를 추가하세요.
solardict['태양']='Sun'

# 2. solardict에 키가 '지구', 값이 'Earth'인 요소를 추가하세요.
solardict['지구']='Earth'

# 3. solardict에 키가 '달', 값이 'Moon'인 요소를 추가하세요.
solardict['달']='Moon'

# 4. 사전, for, enumerate를 이용한 아래 코드를 주석을 읽으며 이해해보세요.
# 영어 단어로 구성된 english 리스트 선언합니다.
english = ['abandon', 'ablaze', 'abnormality', 'abolish']
# 영어 단어 뜻으로 구성된 korean 리스트를 선언합니다.
korean = ['버리다', '불타는', '변칙', '폐지하다']
# 비어있는 vocab 사전을 선언합니다.
vocab = {}
# english 리스트의 인덱스와 요소를 각각 i와 k에 순서대로 저장합니다. 
for i, k in enumerate(english):
    # korean 리스트의 요소값을 val 변수에 순서대로 저장합니다. (val = '버리다')
    val = korean[i]
    # vocab 사전에 english 리스트의 요소를 키로, korean 리스트의 요소를 값으로 추가합니다.
    vocab[k] = val

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(solardict)
print(vocab)


{'태양': 'Sun', '지구': 'Earth', '달': 'Moon'}
{'abandon': '버리다', 'ablaze': '불타는', 'abnormality': '변칙', 'abolish': '폐지하다'}
```


```sh
# 실습에 사용할 변수를 선언합니다.
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
solardict = {'태양':'Sun', '지구':'Earth', '달':'Moon'}

# 1. names의 모든 값을 추출하여 변수 vals1에 저장하세요.
vals1 = names.values()

# 2. vals1에 객체형으로 저장된 names의 모든 값을 리스트형으로 변경한 후 변수 val_list1에 저장하세요.
vals1 = names.values()
val_list1 = list(vals1)

# 3. solardict의 모든 값을 추출하여 변수 vals2에 저장하세요.
vals2 = solardict.values()


# 4. vals2에 객체형으로 저장된 solardict의 모든 값을 리스트형으로 변경한 후 변수 val_list2에 저장하세요.
vals2 =  solardict.values()
val_list2 = list(vals2)

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print('names의 모든 값을 객체형으로 추출합니다:\n>>>', vals1)
print('names의 모든 값을 리스트에 담습니다:\n>>>', val_list1)
print('solardict의 모든 값을 객체형으로 추출합니다:\n>>>', vals2)
print('solardict의 모든 값을 리스트에 담습니다:\n>>>', val_list2)



names의 모든 값을 객체형으로 추출합니다:
>>> dict_values([10999, 2111, 9778, 20245, 27115, 5887, 7855])
names의 모든 값을 리스트에 담습니다:
>>> [10999, 2111, 9778, 20245, 27115, 5887, 7855]
solardict의 모든 값을 객체형으로 추출합니다:
>>> dict_values(['Sun', 'Earth', 'Moon'])
solardict의 모든 값을 리스트에 담습니다:
>>> ['Sun', 'Earth', 'Moon']
```

```sh
# 실습에 사용할 변수를 선언합니다.
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}

# 1. names의 키를 오름차순으로 정렬한 값을 ret1에 저장하세요. 
ret1 = sorted(names)

# 2. names의 키를 내림차순으로 정렬한 값을 ret2에 저장하세요. 
ret2 =  sorted(names, reverse=True)

# 3. names의 값을 오름차순으로 정렬한 값을 ret3에 저장하세요.
ret3 = sorted(names.values())

# 4. names의 모든 요소를 오름차순으로 정렬한 값을 ret4에 저장하세요.
ret4 = sorted(names.items())

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(ret1)
print(ret2)
print(ret3)
print(ret4)


['Aimy', 'Bob', 'Kelly', 'Mary', 'Michale', 'Sams', 'Tom']
['Tom', 'Sams', 'Michale', 'Mary', 'Kelly', 'Bob', 'Aimy']
[2111, 5887, 7855, 9778, 10999, 20245, 27115]
[('Aimy', 9778), ('Bob', 5887), ('Kelly', 7855), ('Mary', 10999), ('Michale', 27115), ('Sams', 2111), ('Tom', 20245)]
```

```sh
# 1. x와 y를 인자로 받아 합을 출력하는 lambda 함수를 정의하고 add에 저장하세요.
add = lambda x, y: x+y

# 2. add를 이용해 1과 3의 합을 출력하세요. 
print(add(1,3))

4
```

```sh
# 실습에 사용할 변수를 선언합니다.
args = [1, 2, 3, 4, 5]

# 1. x를 인자로 받아 x의 제곱 x*x를 리턴하는 lambda 함수를 f에 저장하세요.
f =  lambda x: x*x 

# 2. args의 모든 요소를 f에 대입하여 결과를 얻은 후 ret1에 저장하세요.
ret1 = map(f, args)

# 3. ret1에 저장된 객체를 리스트 형태로 변환하세요.
ret2 = list(ret1)

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(ret2)

[1, 4, 9, 16, 25]
```

```sh
# 1. open()을 이용해 stockcode.txt 텍스트 파일을 읽기 모드로 열고, 파일 객체를 f에 저장하세요.
f = open('stockcode.txt', 'r')

# 2. read()를 이용해 stockcode.txt 파일의 모든 내용을 읽고 data의 저장하세요. 
data = f.read()

# 3. data에 저장된 stockcode.txt 파일의 모든 내용을 출력하세요.
print(data)

# 4. close()를 이용해 stockcode.txt 파일을 닫으세요. 
f.close()


096300 베트남개발1
096760 중외홀딩스
096770 SK에너지
096771 SK에너지우
097230 한진중공업
097950 CJ제일제당
097951 CJ제일제당
097952 CJ제일제당
097953 CJ제일제당
098150 한국아태특별
099210 코리아07호
099340 하나니켈1호
099350 하나니켈2호
100220 비유와상징
100250 진양홀딩스
100840 S&TC
101060 SBS홀딩스
101140 아티스
101380 거북선2호
101790 케이알제2호
101990 파브코
102000 거북선3호
102260 동성홀딩스
102280 트라이
103140 풍산
103150 하이트맥주
103151 하이트맥주우
103160 풀무원
103590 일진전기
104110 신성ENG
104120 신성FA
104700 한국철강
105560 KB금융
107590 미원에스씨
```

```sh
# 실습에 사용할 변수를 선언합니다.
line_num = 1

# 1. open()을 이용해 stockcode.txt 텍스트 파일을 읽기모드로 열고, 파일 객체를 f에 저장하세요.
f = open('stockcode.txt', 'r')

# 2. readline()을 이용해 stockcode.txt 파일 내용의 한 줄을 읽고 line에 저장하세요.
line = f.readline()

# 3. 실행 버튼을 누르고 주석과 함께 코드를 이해해보세요.
# line_num이 6보다 작을 동안 코드블럭을 실행합니다.
while line_num < 6:
    # line_num과 stockcode.txt 파일 내용의 한 줄을 같이 출력합니다.
    print('%d | %s' %(line_num, line), end='')
    # stockcode.txt 파일 내용의 다음 줄을 읽고 line에 저장합니다.
    line = f.readline()
    # line_num에 1을 더합니다.
    line_num += 1
# 파일을 닫습니다.
f.close()



1 | 000020 동화약품
2 | 000040 S&T모터스
3 | 000050 경방
4 | 000060 메리츠화재
5 | 000070 삼양사
```

```sh
# 1. open()을 이용해 stockcode.txt 텍스트 파일을 읽기모드로 열고, 파일 객체를 f에 저장하세요.
f = open('stockcode.txt', 'r')

# 2. readlines()을 이용해 stockcode.txt 파일의 내용을 원소로 갖고 있는 리스트를 lines에 저장하세요. 
lines = f.readlines()

# 3. 실행 버튼을 누르고 주석과 함께 코드를 이해해보세요.
# lines의 인덱스와 요소를 각각 line_num과 line에 순서대로 저장합니다.
for line_num, line in enumerate(lines):
    # 첫번째 반복문에서는 인덱스 0과 000020 동화약품 \n이 line에 저장됩니다.
    print('%d %s' %(line_num+1, line), end='')
# 파일을 닫습니다.
f.close()

921 103590 일진전기
922 104110 신성ENG
923 104120 신성FA
924 104700 한국철강
925 105560 KB금융
926 107590 미원에스씨
```

```sh
# 1. with open() as를 이용해 stockcode.txt 텍스트 파일을 읽기모드로 열고, 파일 객체를 f에 저장하세요.
with open('stockcode.txt', 'r') as f:

# 실습 결과를 출력하는 코드입니다. 수정하지 마세요. 
    for line_num, line in enumerate(f.readlines()):
        print('%d %s' %(line_num+1, line), end='')
        
        
917 103140 풍산
918 103150 하이트맥주
919 103151 하이트맥주우
```

```sh
# 1. stockcode.txt를 읽기 모드로 열고 f에 저장합니다.
f = open('stockcode.txt', 'r')

# 2. stockcode.txt의 105 바이트 위치부터 파일을 읽기 시작하세요.
f.seek(105)

# 3. 500 바이트 만큼 파일을 읽고 그 내용을 data에 저장하세요.
data = f.read(500)

# 4. 파일을 닫으세요.
f.close()

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(data)



000520 삼일제약
000540 흥국쌍용화재
000541 흥국쌍용화재우
000542 흥국쌍용화재2우B
0005
```


```sh
# 1. time 모듈에서 localtime() 함수를 임포트하세요.
from time  import localtime

# 2. localtime()을 이용해 time.struct_time 형식의 현재시간을 user_time에 저장하세요.
user_time = localtime()

# 3. user_time의 인덱스3 값을 hour에 저장하세요.
hour = user_time[3]

# 4. user_time의 인덱스4 값을 minute에 저장하세요.
minute = user_time[4]

# 5. user_time의 인덱스5 값을 sec에 저장하세요.
sec = user_time[5]

# 아래는 출력을 위한 코드입니다. 수정하지 마세요..
print('이 코드는 <%d시 %d분 %d초>에 실행되었습니다 (UTC+09:00).' %(hour+9, minute, sec))

이 코드는 <23시 49분 18초>에 실행되었습니다 (UTC+09:00)
```


```sh
# 1. datetime 모듈에서 datetime 객체를 임포트하세요.
from datetime import datetime

# 2. 현재 시간을 측정하여 start에 저장하세요.
start = datetime.now()

# 아래는 실습에 사용되는 코드입니다. 수정하지 마세요.
ret = 0
for i in range(100000):
    ret += i

# 3. 현재 시간을 다시 측정하여 end에 저장하세요.
end = datetime.now()

# 4. start와 end에 저장된 두 시간의 차이를 계산하고 elapsed에 저장하세요.
elapsed = end-start

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print('1에서 100000까지 더한 결과: %d' %ret)
print('총 계산 시간:', elapsed)



# 1. datetime 모듈에서 datetime 객체를 임포트하세요.
from datetime import datetime

# 2. 현재 시간을 측정하여 start에 저장하세요.
start = datetime.now()

# 아래는 실습에 사용되는 코드입니다. 수정하지 마세요.
ret = 0
for i in range(100000):
    ret += i

# 3. 현재 시간을 다시 측정하여 end에 저장하세요.
end = datetime.now()

# 4. start와 end에 저장된 두 시간의 차이를 계산하고 elapsed에 저장하세요.
elapsed = end-start

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print('1에서 100000까지 더한 결과: %d' %ret)
print('총 계산 시간:', elapsed)

```

```sh
1
# 1. datetime 모듈에서 datetime 객체를 임포트하세요.
2
from datetime import datetime
3
​
4
# 2. 현재 시간을 측정하여 start에 저장하세요.
5
start = datetime.now()
6
​
7
# 아래는 실습에 사용되는 코드입니다. 수정하지 마세요.
8
ret = 0
9
for i in range(100000):
10
    ret += i
11
​
12
# 3. 현재 시간을 다시 측정하여 end에 저장하세요.
13
end = datetime.now()
14
​
15
# 4. start와 end에 저장된 두 시간의 차이를 계산하고 elapsed에 저장하세요.
16
elapsed = end-start
17
​
18
# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
19
print('1에서 100000까지 더한 결과: %d' %ret)
20
print('총 계산 시간:', elapsed)
21
​

실행

제출

질문하기
최종 제출 점수
100
최종 제출 시간
2021.2.15 23:50
실행 결과
코더랜드에 연결되었습니다.

1에서 100000까지 더한 결과: 4999950000
총 계산 시간: 0:00:00.010015
```

**Stack**  

```sh
# 1. 원소를 갖고 있지 않은 빈 리스트를 생성하여 mystack에 저장하세요.
mystack = []

# data를 mystack에 요소로 추가하는 putdata 함수를 정의합니다.
def putdata(data):
    # 2. 전역변수 mystack에 접근하세요.
    print(mystack)
    
    # 3. mystack 리스트에 putdata 함수의 인자인 data를 맨 마지막 요소로 추가하세요.
    mystack.append(data)
    

# 요소를 mystack으로부터 하나 추출하는 함수 popdata를 정의합니다.
def popdata():
    # 전역변수 mystack에 접근합니다.
    global mystack
    # mystack의 크기가 0이면, 즉 추출할 데이터가 없으면 None을 리턴합니다. 
    if len(mystack) == 0:
        return None
    # mystack에 데이터가 있으면 mystack.pop()을 리턴합니다.
    return mystack.pop()

# 위에서 정의한 putdata를 이용해 문자열, 리스트, 숫자를 mystack에 추가해봅니다.
putdata('데이터1')
putdata([3, 4, 5, 6])
putdata(12345)

# mystack에 저장된 원소를 확인하기 위해 출력해봅니다.
print('<스택상태>: ', end=''); print(mystack)

# popdata()를 호출하여 mystack에서 데이터를 하나 추출하여 ret에 저장합니다.
ret = popdata()
# ret이 None일 때까지 popdata()를 호출하여 mystack으로부터 원소를 하나씩 추출합니다.
while ret != None:
    # mystack에서 추출된 원소를 출력합니다.
    print('스택에서 데이터 추출된 원소: ', end=''); print(ret)
    # mystack에서 원소가 추출된 후 mystack에 저장된 원소를 출력합니다.
    print('<스택상태>: ', end=''); print(mystack)
    ret = popdata()
    
    
    
[]
['데이터1']
['데이터1', [3, 4, 5, 6]]
<스택상태>: ['데이터1', [3, 4, 5, 6], 12345]
스택에서 데이터 추출된 원소: 12345
<스택상태>: ['데이터1', [3, 4, 5, 6]]
스택에서 데이터 추출된 원소: [3, 4, 5, 6]
<스택상태>: ['데이터1']
스택에서 데이터 추출된 원소: 데이터1
<스택상태>: []
```

```sh
# 1. filename과 word를 인자로 받는 countWord 함수를 정의하세요.
def countWord(filename, word) :
    # 2. with open() as를 이용해 인자로 받은 filname을 읽기모드로 열고 파일 객체를 f에 저장하세요.
    with open(filename, 'r') as f:
        # 3. read()를 이용해 인자로 받은 filename 파일의 모든 내용을 읽고 text에 저장하세요.
        text = f.read()
        # 4. text에 저장된 모든 문자를 소문자로 변경한 후 text에 다시 저장하세요.
        text = text.lower()
        # text에서 word가 최초로 나타나는 위치를 구하여 pos에 저장합니다.
        pos = text.find(word)
        # 단어의 개수를 담을 변수 count를 선언합니다.
        count = 0
        # find()는 찾고자 하는 문자열이 없을 경우 -1을 리턴합니다. 해당 단어를 찾지 못할 때까지 반복합니다. 
        while pos != -1:
            # 문자열이 존재할 경우 count를 1 증가합니다.
            count += 1
            # word의 위치 다음부터 다시 text에서 word를 찾습니다.
            pos = text.find(word, pos+1)
    return count

word = 'python'
# python.txt에서 'python'이 등장하는 빈도수를 ret에 저장합니다.
ret = countWord('python.txt', word)
# ret에 저장된 python의 빈도수를 출력합니다.
print('[%s]의 개수: %d' %(word, ret))


[python]의 개수: 32
```

