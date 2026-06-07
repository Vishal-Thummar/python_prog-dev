flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi", "Cardamom"]
for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        print(f"{flavour} is available")
        break
    print(f"{flavour} item found")
print(f"Out side of loop")
