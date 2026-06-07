# value = 13
# remainder = value % 5

# if remainder:
#     print(f"NOt divisible , remainder is {remainder}")

# value = 14

# if (remainder := value % 5):
# print(f"NOt divisible , remainder is {remainder}")

# serving_chai = ["small","medium","large"]

# if (requested_chai := input("Enter Cup size : ")) in serving_chai:
#     print(f"Serving {requested_chai} chai")
# else:
#     print(f"Size is unavailable - {requested_chai}")


flavors = ["lamon", "Litchi", "mango", "orange", "apple"]

while (flavor := input("Choose your flavour : ")) not in flavors:
    print(f"You Choose Wrong {flavor} is is not avaiable")
print(f"You choose {flavor}")
