class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)

    def display_cart(self):
        if not self.cart_items:
            print("Korpa je prazna.")
        else:
            print("Sadržaj korpe:")
            for item in self.cart_items:
                print(item.display_info())

    def total_cart_value(self):
        return sum(p.price * p.quantity for p in self.cart_items)