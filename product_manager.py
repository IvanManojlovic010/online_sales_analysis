from product import Product

class ProductManager:
    def __init__(self):
        # lista svih dostupnih proizvoda
        self.products = []

    def add_product(self, product):
        # dodavanje proizvoda u listu
        self.products.append(product)

    def display_products(self):
        # prikaz svih proizvoda
        for p in self.products:
            print(p.display_info())

    def total_value(self):
        # prikaz ukupne vrednosti svih proizvoda
        return sum(p.price * p.quantity for p in self.products)