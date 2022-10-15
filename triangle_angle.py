#Write a Python program to check whether the triangle is valid or not if sides are given.

a = int(input('Enter length of Angle a: '))
b = int(input('Enter length of Angle b: '))
c = int(input('Enter length of Angle c: '))


if a+b+c == 180:
    print('Triangle is valid')

else:
    print('Triangle is Invalid.')