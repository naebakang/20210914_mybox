# File encoding: utf8

print(1)

12345 + 1234

23412323 / 545545

[1, 2, 3, 4, 5]

a = [1, 2, 3, 4, 5]

print(a)

num1 = 123454543544
num2 = 47474747474474723

num1 + num2

list1 = [1, 2, 3, 4, 5]

list1[-2]

list2 = [34, 67, 98, 383838, 9556744]

for i in list2:
    print(i)

num = 229
if num > 100 and num > 99:
    print(1234)

list_score = [23, 67, 98, 23, 13, 76, 67, 55]
A = []
B = []
C = []
for i in list_score:
    if 80 <= i:
        A.append(i)

    elif 60 <= i < 80:
        B.append(i)
    else:
        C.append(i)
print('A반: {}'.format(A))
print('B반: {}'.format(B))
print('C반: {}'.format(C))

import re

text = 'apple, banana, watermelone, melone'
pattern = re.compile('...na')
pattern.search(text)

pattern.findall(text)

aa = '철수는 꽃무늬티셔츠를 입엇고, 영희는 민무늬티셔츠를 입었고, 그렇다면 줄무늬 티셔츠는 누가 입었을까?'
pattern = re.compile('...티셔츠')
pattern.findall(aa)

pattern2 = re.compile('티*셔츠')
text1 = '셔츠, 티셔츠, 티티셔츠, 티티티셔츠, 티티티티티티티팉셔츠'
pattern2.findall(text1)

pattern3 = re.compile('티+셔츠')
pattern3.findall(text1)

pattern4 = re.compile('.+셔츠')
pattern4.findall(text1)

pattern5 = re.compile('[가-힣]+셔츠')
pattern5.findall(text1)

text2 = '꽃무늬티셔츠, 민무늬티셔츠, 1988티셔츠, U넥티셔츠, v넥티셔츠'
pattern6 = re.compile('[가-힣0-9a-zA-Z]+셔츠')
pattern6.findall(text2)

text3 = '우리집에는 개가 5마리, 소 24마리, 돼지 8마리, 닭 102마리'
pattern7 = re.compile('\d{1,3}')
pattern7.findall(text3)

price = '<li id="normal_price" style="display: none;">65000</li>'
pattern8 = re.compile('\d{1,10}')
pattern8.findall(price)

price = '1,120,000원<del>268,000원<>49,000원'
pattern9 = re.compile('[0-9,]+원')
pattern9.findall(price)
