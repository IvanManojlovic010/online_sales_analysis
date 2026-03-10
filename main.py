from product import Product
from product_manager import ProductManager

# Kreiranje ProductManager‑a
manager = ProductManager()

# Dodavanje nekoliko proizvoda
manager.add_product(Product("Gaming Laptop", 55555, 5))
manager.add_product(Product("Telefon Samsung", 25000, 33))
manager.add_product(Product("Slusalice", 2000, 10))

# Prikaz svih proizvoda
print("Lista proizvoda:")
manager.display_products()

# Prikaz ukupne vrednosti inventara
print("Ukupna vrednost inventara:", manager.total_value(), "RSD")

# Uklanjanje proizvoda
manager.remove_product("Telefon")
print("\nNakon uklanjanja proizvoda:")
manager.display_products()