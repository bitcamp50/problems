def calculate_total(price, quantity):
    return price * quantity

def main():
    items = 3
    subtotal = 0

    for i in range(1, items + 1):
        price = float(input(f"Enter the price of item {i}: "))
        quantity = int(input(f"Enter the quantity of item {i}: "))
        subtotal += calculate_total(price, quantity)

    tax_rate = 0.055
    tax = subtotal * tax_rate
    total = subtotal + tax

    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")

if __name__ == "__main__":
    main()
