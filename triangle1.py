#Write a Python program to check whether the triangle is valid or not if sides are given.

a = int(input('Enter length of side a: '))
b = int(input('Enter length of side b: '))
c = int(input('Enter length of side c: '))


if a+b>=c and b+c>=a and c+a>=b:
    print('Triangle is valid')

else:
    print('Triangle is Invalid.')