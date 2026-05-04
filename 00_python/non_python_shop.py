class Chai:
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level

    def sip(self):
        print("Sipping...")

    def add_sugar(self, amount):
        print("added the sugar..")


myChai = Chai(sweetness=3, milk_level=4)
myChai.add_sugar(5)
