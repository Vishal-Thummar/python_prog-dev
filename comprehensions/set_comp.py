favorite_chais = [
    "masala chai",
    "ginger chai",
    "masala chai",
    "cardamom chai",
    "assertive chai",
    "green tea",
    "black chai",
    "green tea",
]


# unique_chia = { chai for chai in favorite_chais if len(chai) > 120 }
unique_chia = {chai for chai in favorite_chais}
# print(unique_chia)


recipes = {
    "chai": ["ginger chai", "masala chai", "cardamom chai"],
    "tea": ["green tea", "black tea", "orange juice", "ginger chai"],
    "juice": ["apple juice", "orange juice"],
}
unique_spices = {spice for ingrerdients in recipes.values() for spice in ingrerdients}

# print(unique_spices)


tea_prices_inr = {
    "masala chai": 10,
    "ginger chai": 15,
    "cardamom chai": 20,
    "green tea": 12,
    "black chai": 18,
}
tea_prices_usd = {tea: price / 80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)
