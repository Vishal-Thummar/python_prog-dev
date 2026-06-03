snack = input("Enter your Preferred snack: ").lower()


if snack == "samosa" or snack == "cookies":
    print("Great Choice {}".format(snack))
else:
    print("Sorry we have Only server cookies and samosa with tea")