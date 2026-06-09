def chai_cussstomer():
    print("Welcome to chai stall")
    order = yield
    while True:
        print(f"Your chai order is {order}")
        order = yield


stall = chai_cussstomer()
next(stall)
stall.send("Lemon")
stall.send("Mango")
