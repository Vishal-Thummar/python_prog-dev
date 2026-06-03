order_amount  = int(input("Enter Your Order Amont : ₹"))
# order_amount  = input("Enter Your Order Amont : ₹")
print(f"tea order amount is ₹{type(order_amount)} ")

delivery_fees = 0 if order_amount > 300 else 30
print(f"your delivery fees is ₹{delivery_fees}")