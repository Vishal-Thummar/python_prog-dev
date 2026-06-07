# def make_chai():
#     return "Here is yout Tea"

# print(make_chai())


# None
def idle_teaworker():
    pass


print(idle_teaworker())


# One value
def sold_cup():
    return 120


total = sold_cup()
print(total)


# Early from a function
def chai_status(chai_left):
    if chai_left == 0:
        return "sorry chai over"
    return "Chai is available"
    print("Chai is available")


print(chai_status(0))
print(chai_status(1))


# Multiple values

# def chai_report():

#     return 100,200 ,899# sold , remaining
# sold , remaining,_= chai_report()
# print("sold is " ,sold)
# print("remaining is : ",remaining)


# Multiple values


def chai_report():

    return 100, 200, 899  # sold , remaining


sold, remaining, not_paid = chai_report()
print("sold is ", sold)
print("remaining is : ", remaining)
