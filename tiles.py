# program that calculate the no of rectangle tiles required to cover a rectungular floor if the
# dimension of the floor and the dimensions of a tiles are entered by the user?
l=int(input("enter length of room"))
w=int(input("enter width of room"))
l1=int(input("enter length of tile"))
w1=int(input("enter width of room"))
f1= l*w
f2=l1*w1
f3=f1/f2
r=int(f3+.999)
print("no of tiles are ",r)

#or
'''
l=int(input("enter length of room"))
w=int(input("enter width of room"))
l1=int(input("enter length of tile"))
w1=int(input("enter width of room"))
f1= l*w
f2=l1*w1
f3=-(-f1//f2)

print("no of tiles are ",f3)
