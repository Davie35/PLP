# Function to calculate discounted price
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (price * discount_percent) / 100
        return price - discount_amount
    else:
        return price  # return original price if discount < 20%


# Main program
try:
    # Prompt user for input
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Call the function
    final_price = calculate_discount(price, discount_percent)

    # Display results
    if discount_percent >= 20:
        print(f"Discount applied! Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Original price: ${price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values.")
