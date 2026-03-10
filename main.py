from product import Product
from product_manager import ProductManager

# Kreiranje ProductManager‑a
manager = ProductManager()

# Dodavanje nekoliko proizvoda
manager.add_product(Product("Laptop", 50000, 2))
manager.add_product(Product("Telefon", 20000, 3))
manager.add_product(Product("Slusalice", 3000, 10))

# Prikaz svih proizvoda
print("Lista proizvoda:")
manager.display_products()

# Prikaz ukupne vrednosti inventara
print("Ukupna vrednost inventara:", manager.total_value(), "RSD")