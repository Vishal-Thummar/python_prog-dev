chai_order = dict(type="Masala Chai",size="large",sugar=2)

print(f"Chai Order in Dict {chai_order}")


chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base {chai_recipe["base"]}")
del chai_recipe["liquid"]
print(f"Recipe final {chai_recipe}")

print(f"Is Sugar in the Order? {'sugar' in chai_order} ")

chai_order = {"type" :"Ginger Tea","Size":"Medium","Sugar":4}
print(f"Chai Order is {chai_order}")

print(chai_order.keys())
print(chai_order.values())
print(chai_order.items())

print(f"chai_recipe is {chai_recipe}")
last_item = chai_order.popitem()
print(last_item)

extra_spices = {"cardamom":"crushed","ginger":"sliced"}
chai_recipe["liquid"] = "milk"
print(f"Chai Recipe is {chai_recipe}")
chai_recipe.update(extra_spices)
print(f"Chai Recipe is {chai_recipe}")
chai_size = chai_order["Size"]
print(chai_size)


chai_order["note"] = "Extra Sugar"
customer_note = chai_order.get("note","No Note")
print(customer_note)