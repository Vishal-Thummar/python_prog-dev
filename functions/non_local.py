def chai_order():
    chai_type = "lemon"

    def kitchen():
        nonlocal chai_type
        chai_type = "masala"

    kitchen()
    print("after kitchen update ", chai_type)


chai_order()
