# temperature = 40
# while temperature < 100:
#     print(f"Temperature is {temperature}")
#     # temperature = temperature + 15
#     temperature += 15

# print(f"boiled water ready to serve")


# Initialize account balance and withdrawal tracking
balance = 10000
withdrawals = []  # List to store withdrawal amounts
result = []  # List to store transaction results

# Define withdrawal amounts to process
withdrawals = [1000, 1500, 2000, 3000, 1500, 10]
# Process each withdrawal request
index = 0
while index < len(withdrawals):
    amount = withdrawals[index]

    # Check if sufficient funds are available for the withdrawal
    if amount <= balance:
        # Process successful withdrawal
        balance -= amount
        result.append(f"Withdrawn: {amount}")
    else:
        # Handle insufficient funds case
        result.append(f"Insufficient funds for requested amount: {amount}")

    # Move to next withdrawal request
    index += 1

# Add final balance to results
result.append(f"Remaining Balance: {balance}")

# Display all transaction results
for transaction in result:
    print(transaction)


# atm cash withdrawal
# amount
# session
# request per withdrawal
# first check if the request withdrawal amount less then available balance
# if yes then proceed
# else show insufficient funds
# end of session show remaining balance

# if balance greater then requested as per request amount
# then proceed
# else show insufficient funds
