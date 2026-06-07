# chai_type = "Ginger Chai"
# customer_name = "Jaya"

# print(f"Order for {customer_name} : {chai_type} please !")

# chai_description = "Aromatic and Bold"
# print(f"First Word : {chai_description[0:3]}")


# # lable_text = "Chai Spèčial"
# lable_text = "Chai Special"
# encoded_lable = lable_text.encode("utf-8")
# print(encoded_lable)
# decoded_lable = encoded_lable.decode("utf-8")
# print(decoded_lable)


is_sunny = True
have_umbrella = False

print(f"Is it not sunny today? {not is_sunny}")
print(f"Do You not have an umbrella? {not have_umbrella}")
print(
    f"Should you go for a walk if it’s sunny and you don’t need an umbrella? {is_sunny and not have_umbrella}"
)
print(
    f"Should you go for a walk if it’s sunny or if you have an umbrella? {is_sunny or have_umbrella}"
)
