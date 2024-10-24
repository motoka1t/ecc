from FieldElement import *

# 1.3.1
a = FieldElement(7, 13)
b = FieldElement(6, 13)
print(a==b)
print(a==a) 

# 1.4.1
print(7%3)

print(-27 % 13)

# 練習問題2
prime = 57
print((44 + 33)%prime)
print((9-29)%prime)
print((17 + 42 + 49)%prime)
print((52 - 30 - 38)%prime)

# 1.5.1
a = FieldElement(7, 13)
b = FieldElement(12, 13)
c = FieldElement(6, 13)
print(a+b==c)

#練習問題4
prime = 97
print((95*45*31)%prime)
print((17**13*19*44)%prime)
print((12**7*77**49)%prime)

#練習問題5
prime = 19
for k in (1,3,7,13,18):
    print([k*i % prime for i in range(prime)])
for k in (1,3,7,13,18):
    print(sorted([k*i % prime for i in range(prime)]))

#1.6.1
a = FieldElement(3,13)
b = FieldElement(12, 13)
c = FieldElement(10,13)
print(a*b==c)

#1.6.2
a = FieldElement(3,13)
b = FieldElement(1,13)
print(a**3==b)

#練習問題7
for prime in (7, 11, 17, 31):
    print([pow(i, prime-1, prime) for i in range(1, prime)])

#練習問題8
prime = 31
print(3*pow(24, prime-2, prime)%prime)
print(pow(17, prime-4, prime))
print(pow(4, prime-5, prime)*11 % prime)

#1.8
a = FieldElement(7, 13)
b = FieldElement(8, 13)
print(a**-3==b)