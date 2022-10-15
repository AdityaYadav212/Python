x=int(input('Enter the number : '))
n=x
a=x%10
x=x//10
b=x%10
x=x//10
rev= a*100+b*10+x

if n==rev:
    print ( 'number is plandrom' , rev)

else :

 print(rev)