#Write a Python program to check whether the triangle is valid or not if sides are given.

a = int(input('Enter length of side a: '))
b = int(input('Enter length of side b: '))
c = int(input('Enter length of side c: '))


if a==b or b==c or c==a:
    print('Triangle is isolateral')

elif a==b==c:
    print('Triangle is Equalateral.')

else:
    print('Triangle is scalateral')