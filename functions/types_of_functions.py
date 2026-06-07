# pure functions

# def pure_chai(cups):
#     return cups + 90

# total_chai= 0


# # Not Good Thingss
# def impure_chai(cups):
#     global total_chai
#     total_chai += cups


# Recursive Function
def pour_chai(n):
    print(n)
    if n == 0:
        return "All Cups poured"
    return pour_chai(n - 1)


print(pour_chai(4))


chai_tyes = ["tulsi", "oolung", "ginger", "cardamom", "ginger"]
strong_chai = list(filter(lambda chai: chai != "ginger", chai_tyes))
print(strong_chai)
