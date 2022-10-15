'''
# write a program to define the no as even or odd 

a=int(input("enter the no."))
if  a%2==0:
           print("the no is even")
else:
           print("the no is odd")
'''

a=int(input("value"))
out=['even','odd'][a%2]
print(out)