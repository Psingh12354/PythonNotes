price=int(input("Enter the price : "))
quantity=int(input("Enter quantity : "))
amount=price*quantity
if amount>1000:
    print("You got a discount of 10%")
    discount=amount*10/100
    amount-=discount
else:
    print("You got a discount of 5%")
    discount=amount*5/100
    amount-=discount
print("Total amount is : ",amount)
