 
total=0
for counter in range(1,11):
    price = float(input("Enter item price \n"))
while price<0:# using a while loop for validation
    print("Enter a valid price  (>=0)")
    price = float(input("Enter item price \n"))
total = total+price
print("Total price for ten items is kshs{total:.2sf}" )
