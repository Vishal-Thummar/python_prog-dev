# def generate_invoice(customer_name: str = "Guest", *items: str, **charges: float) -> str:
#     # Write your code below this line
#     total = 0.0
#     invoice_lines = [f"Invoice for {customer_name}:"]

#     if items:
#         invoice_lines.append("Items:")
#         for item in items:
#             invoice_lines.append(f"- {item}")

#     if charges:
#         invoice_lines.append("Charges:")
#         for label, amount in charges.items():
#             invoice_lines.append(f"{label.capitalize()}: {amount}")
#             total += amount

#     invoice_lines.append(f"Total Amount Due: {total}")
#     return "\\n".join(invoice_lines)


def generate_invoice(
    customer_name: str = "Guest", *items: str, **charges: float
) -> str:
    lines = []

    # Header
    lines.append(f"Invoice for {customer_name}")

    # Items Section (only if items are provided)
    if items:
        lines.append("Items:")
        for item in items:
            lines.append(f"- {item}")

    # Charges Section (only if charges are provided)
    if charges:
        lines.append("Charges:")
        for charge_name, amount in charges.items():
            # Capitalize charge name
            capitalized_charge = charge_name.capitalize()
            lines.append(f"{capitalized_charge}: {amount}")

    # Calculate total from charges onlycc
    total = sum(charges.values())
    lines.append(f"Total Amount Due: ₹{total}")

    # Join all lines with newline character
    return "\n".join(lines)


# Run the function with example arguments
result = generate_invoice("John Doe", "Banana", "Apple", tax=10.0, shipping=5.0)
print(result)
