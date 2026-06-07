def serve_chai():
    chai_type = "Masala Chai"  # Local Scope
    print(f"Inside Function Chai Type is {chai_type}")


chai_type = "lemon"
serve_chai()
print("Outside Function Chai Type is " + chai_type)


def chai_counter():
    chai_order = "lemon"  # Enclosing

    def print_order():
        chai_order = "oolang"
        print("inner chai order is " + chai_order)

    print_order()
    print("outer chai order is " + chai_order)


chai_order = "Tulsi"  # Global Scope
chai_counter()
print("Global , chai order is " + chai_order)
