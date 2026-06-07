# chai = "GInger"

# def prepared_chai(order):
#     print(f"Chai type is {order}")


# prepared_chai(chai)
# print(f"Global Chai type is {chai}")

chai = [1, 2, 3, 4]


# def edit_chai(cup):
#     cup[1] = 43

# edit_chai(chai)
# print(chai)


# def make_chai(tea,milk,sugar):
#     print(tea, milk, sugar)

# make_chai("Green","Yes","Medium")
# make_chai(milk="No",tea="Oolang",sugar=3)


# def special_chai(*ingrediants,**extras):
#     print("Ingrediants :",ingrediants)
#     print("Extras ",extras)

# special_chai("Cinnamon","Cardamon",sweetner= "honey",foam="yes")


# def chai_order(order=[]):
#     order.append("New Order")
#     print(order)
def chai_order(order=None):
    if order is None:
        order = []
        order.append("New Order")
    print(order)


chai_order()
