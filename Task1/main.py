
def get_user_input():
    while True:
        try:
            pizzas_ordered = int(input("How many pizzas ordered? "))
            if pizzas_ordered < 0:
                raise ValueError("Please enter a positive integer!")

            delivery_required = input("Is delivery required? (Y/N) ").strip().lower()
            if delivery_required not in ['y', 'n']:
                raise ValueError('Please answer "Y" or "N".')

            is_tuesday = input("Is it Tuesday? (Y/N) ").strip().lower()
            if is_tuesday not in ['y', 'n']:
                raise ValueError('Please answer "Y" or "N".')

            used_app = input("Did the customer use the app? (Y/N) ").strip().lower()
            if used_app not in ['y', 'n']:
                raise ValueError('Please answer "Y" or "N".')

            return pizzas_ordered, delivery_required, is_tuesday, used_app

        except ValueError as e:
            print(e)

def calculate_total_price(pizzas_ordered, delivery_required, is_tuesday, used_app):
    pizza_price = 12
    total_price = pizzas_ordered * pizza_price

    if is_tuesday == 'y':
        tuesday_discount = total_price * 0.5
        total_price -= tuesday_discount  # 50% discount on Tuesdays
        print(f"Tuesday Discount: £{tuesday_discount:.2f}")

    if delivery_required == 'y':
        delivery_cost = 2.5
        if pizzas_ordered >= 5:
            delivery_cost = 0  # Free delivery for 5 or more pizzas
        total_price += delivery_cost
        print(f"Delivery Cost: £{delivery_cost:.2f}")

    if used_app == 'y':
        app_discount = total_price * 0.25
        total_price -= app_discount  # 25% additional discount for app users
        print(f"App Discount: £{app_discount:.2f}")

    return round(total_price, 2)

print("BPP Pizza Price Calculator")
print("==========================")

pizzas_ordered, delivery_required, is_tuesday, used_app = get_user_input()

total_price = calculate_total_price(pizzas_ordered, delivery_required, is_tuesday, used_app)

print(f"\nTotal Price: £{total_price:.2f}.")



