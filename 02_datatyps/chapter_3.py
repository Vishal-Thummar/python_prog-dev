# Integer
black_tea_grams = 15
ginger_grams = 3
total_grams = black_tea_grams+ginger_grams
print(f"Total Grams Base Tea is : {total_grams}")

remainig_tea = black_tea_grams - ginger_grams
print(f"Total grams Remaing : {remainig_tea}")

milk_liters = 7
servings = 4
milk_per_servings = milk_liters / servings
print(f"Milk Per servings : {milk_per_servings}")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"Whole Tea bages per pot : {bags_per_pot}")

total_Cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_Cadamom_pods % pods_per_cup
print(f"leftOver Pods : {leftover_pods}")


base_flavor_strength =2
scale_factor = 3
powerful_flavor = base_flavor_strength ** scale_factor
print(f"PowerFul Flavor : {powerful_flavor}")

total_tea_leaves_harvested = 1_000_000_000
print(f"tea leaves : {total_tea_leaves_harvested}")


#Boolean Logical Operations

is_boiling = True
print(f"Is Water Boiling : {is_boiling}")

stri_count = 5
total_actions = stri_count + is_boiling # Upcastings
print(f"Total Actions : {total_actions}")


milk_present = 0 # No Milk
print(f"Is there Milk? : {bool(milk_present)}")

# And , Or , Not
water_hot = True
tea_added = False

can_serve = water_hot and tea_added
print(f"Can Serve chai? {can_serve}")