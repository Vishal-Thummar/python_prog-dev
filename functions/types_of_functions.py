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


def factorial_recursive(n):
    # Print the current value of n being processed
    print(f"Calculating factorial for: {n}")

    if n < 0:
        print("Error: Negative number provided")
        return "Factorial not dedfined foor nagative number"

    if n == 0 or n == 1:
        print(f"Base case reached: {n}! = 1")
        return 1

    result = n * factorial_recursive(n - 1)
    print(f"Returning: {n}! = {result}")
    return result


print(f"Final result: {factorial_recursive(5)}")


def square_list(nums):
    return list(map(lambda x: x ** 2, nums))
