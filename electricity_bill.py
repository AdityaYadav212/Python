u = int(input('Enter The Amount Of Units Consumed:'))

if u <= 50:

 amt = u*0.5

 print('Amount To Be Paid Is:',amt)

elif u <= 150 and u > 50:

 amt = (50*0.5) + ((u-50)*0.75)

 print('Amount To Be Paid Is:',amt)

elif u <= 250 and u > 150:

 amt = (50*0.5) + (100*0.75) + ((u-150)*1.2)

print('Amount To Be Paid Is:',amt)

else:

amt = (50*0.5) + (100*0.75) + (100*1.2) + ((u-250)*1.5)

print('Amount To Be Paid Is:',amt)

print('Process Completed')