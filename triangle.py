# Validity of Triangle given sides

# Function definition to check validity
def is_valid_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False


a = float(input('Enter length of side a: '))
b = float(input('Enter length of side b: '))
c = float(input('Enter length of side c: '))

# Function call & making decision

if is_valid_triangle(side_a, side_b, side_c):
    print('Triangle is Valid.')
else:
    print('Triangle is Invalid.')