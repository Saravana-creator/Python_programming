amount=int(input("Enter the total amount spend :"))
discount=(0.1 if amount>500 else 0)
total_amt=amount-(amount*discount)
print("The total amount is :",total_amt)