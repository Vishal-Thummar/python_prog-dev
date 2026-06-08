def chai_flavoor(flavor="masala"):
    # chai = true
    """Return the flavor of chai."""
    return flavor
print(chai_flavoor.__doc__)
print(chai_flavoor.__name__)

# help(len)

def generate_bill (chai=0,ice=0):
    """
    calculate the tota bill for chaii and ice
    : param chai : Number oof hai cups (10 rupees each)
    :param ice : Number of ice cream (20 rupees each)
    :return: Total bill amount
    """
    total = (chai*10) + (ice*20)
    return total , "Thank You for visit"




x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()

outer()




