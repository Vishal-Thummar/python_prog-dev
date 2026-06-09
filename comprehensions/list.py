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

# print(iced_tea)


def filter_inventory(
    items: list[dict],
) -> tuple[list[str], set[str], dict[str, int], list[int]]:
    items = [
        {"name": "Notebook", "price": 250, "category": "Stationery"},
        {"name": "Pen", "price": 100, "category": "Stationery"},
        {"name": "Bag", "price": 1200, "category": "Accessories"},
        {"name": "Bottle", "price": 400, "category": "Utensils"},
    ]
    affordable = [item["name"] for item in items if item["price"] > 500]
    categories = {item["category"] for item in items}
    price_map = {item["name"]: item["price"] for item in items}
    discounted_prices = list((int(item["price"] * 0.9) for item in items))
    print(
        f"Afforadbale Items: {affordable} \nCategories: {categories} \nPrice Map: {price_map} \nDiscounted Prices: {discounted_prices}"
    )  # print(      "affordable, categories, price_map, discounted_prices)
    return (affordable, categories, price_map, discounted_prices)


filter_inventory([])
