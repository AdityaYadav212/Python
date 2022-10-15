a=int(input("enter the amount"))
t=2000
f=500
tf=200
o=100
f1= a//t
f2=(a%t)//f
f3=((a%t)%f)//tf
f4=(((a%t)%f)%tf//o)

print("no. of two thousand notes",f1)
print("no. of five hundred notes",f2)
print("no. of two hundred notes",f3)
print("no. of one hundred notes",f4)