def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

#### Calculate the final price after applying the discount
def calculate_discount(original_price, discount_percent):
    discount_amount = original_price * (discount_percent / 100)
    final_price = original_price - discount_amount
    return final_price

# Print the final price
print("Final price after discount:", final_price)
