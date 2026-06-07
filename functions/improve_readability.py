def calculate_bills(cups, price_per_cup):
    return cups * price_per_cup


my_bill = calculate_bills(3, 15)
print(my_bill)


print("order for tabel 2 :", calculate_bills(4, 20))
