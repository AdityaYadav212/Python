#program to input the no of overs in a cricket match and output the maximum runs a player can score in the match . assume 
#that there are no extra or no balls in the match played . for example ,in a 50 over match , the maximum runs scored are1653?

a=int(input("enter no of overs"))
runs=((a-1)*33+36)
print ("max runs scored are",runs)