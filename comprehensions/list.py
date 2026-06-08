menu = [
    "masala chai",
    "ginger chai",
    "plain chai",
    "cardamom chai",
    "assertive chai jaggu",
    "green tea",
    "black chai",
]


# iced_tea = [tea for tea in menu if "chai" in tea]
iced_tea = [tea for tea in menu if len(tea) < 10]

print(iced_tea)
