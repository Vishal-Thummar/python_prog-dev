users = [
    {"id": 1, "total": 200, "coupan": "10%", "name": "Mayur", "age": 22},
    {"id": 2, "total": 300, "coupan": "20%", "name": "Ajit", "age": 23},
    {"id": 3, "total": 400, "coupan": "30%", "name": "Mojo", "age": 24},
    {"id": 4, "total": 500, "coupan": "40%", "name": "Dealan", "age": 25},
    {"id": 5, "total": 600, "coupan": "50%", "name": "Elan", "age": 26}
]
discounts = {
    "10%": (0.1,10),
    "20%": (0.2, 20),
    "30%": (0.3, 30),
    "40%": (0.4, 40),
    "50%": (0.5, 50)
}

for user in users:
    percentaage , fixed = discounts.get(user["coupan"],(0,0))
    discount = user["total"] * percentaage + fixed
    print(f"User Id is {user["id"]} paid {user["total"]} got discount for next visit {discount}")