# Global variable to track total loyalty points earned by all customers
loyalty_points = 0


def process_transactions(transactions: list[int]) -> int:
    # Initialize local variable to store sum of customer's transactions
    total = sum(transactions)

    # Nested function to apply bonus logic
    def apply_bonus():
        nonlocal total
        # If total exceeds ₹1000, add a bonus of ₹50
        if total > 1000:
            total += 50

    # Apply bonus if applicable
    apply_bonus()

    # Update global loyalty points (1 point for every ₹100 spent)
    global loyalty_points
    loyalty_points += total // 100

    # Return the final amount including bonus if applicable
    return total


# Example execution: Running the function with sample transactions
# Test case 1: transactions totaling more than ₹1000
result1 = process_transactions([500, 600])
print(f"Result 1: ₹{result1}, Loyalty Points: {loyalty_points}")

# Test case 2: transactions totaling less than ₹1000
result2 = process_transactions([300, 400])
print(f"Result 2: ₹{result2}, Loyalty Points: {loyalty_points}")
