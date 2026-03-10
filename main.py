from product import Product
from product_manager import ProductManager
from cart import Cart
import random

# Kreiranje ProductManager-a
manager = ProductManager()

# Dodavanje nekoliko proizvoda
manager.add_product(Product("Gaming Laptop", 55555, 5))
manager.add_product(Product("Telefon Samsung", 25000, 33))
manager.add_product(Product("Slusalice", 2000, 10))

print("Lista proizvoda:")
manager.display_products()
print("Ukupna vrednost inventara:", manager.total_value(), "RSD")

# Test remove_product - uklanjanje jednog proizvoda iz inventara
manager.remove_product("Telefon")
print("\nNakon uklanjanja telefona:")
manager.display_products()

# Kreiranje liste svih komada (svaki quantity se razbije na pojedinačne proizvode)
all_items = []
for product in manager.products:
    for _ in range(product.quantity):
        all_items.append(Product(product.name, product.price, 1))

# Kreiranje korpe
cart = Cart()

# Dodavanje 3 slučajno odabrana komada u korpu
for item in random.sample(all_items, 3):
    cart.add_to_cart(item)

# Prikaz sadržaja korpe
print("\nSadržaj korpe:")
cart.display_cart()
print("Ukupna vrednost korpe:", cart.total_cart_value(), "RSD")

# Kreiranje liste svih komada (svaki quantity se razbije na pojedinačne proizvode)
all_items = []
for product in manager.products:
    for _ in range(product.quantity):
        all_items.append(Product(product.name, product.price, 1))

# Kreiranje korpe
cart = Cart()

# Dodavanje 3 slučajno odabrana komada u korpu
for item in random.sample(all_items, 3):
    cart.add_to_cart(item)

# Prikaz sadržaja korpe
print("\nSadržaj korpe:")
cart.display_cart()
print("Ukupna vrednost korpe:", cart.total_cart_value(), "RSD")