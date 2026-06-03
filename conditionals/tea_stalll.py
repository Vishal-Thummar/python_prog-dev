# cup_choice = ["small", "medium", "large"]
# print(cup_choice)
cup_size = input("Enter a Cup Size small/medium/large To Check it Price: ").lower()
print(cup_size)

if cup_size == "small":
    print("Price is ₹10")


elif cup_size == "medium":
    print("Price is ₹15")


elif cup_size == "large":
    print("Price is ₹20")

else:
    print("Invalid Cup Size")
