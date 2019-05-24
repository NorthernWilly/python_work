product = input("Enter Product name:")
price = input("Enter Price:")
qty = input("Enter Quantity:")

cost = int(qty)*float(price)
VAT = cost * 15/100
bill = cost + VAT

print("Your Bill is:")
print("--------------------------")
print("Product:",product)
print("Cost",cost,"VAT",VAT)
print("BILL",bill)
print("--------------------------")
