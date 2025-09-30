from product import Product
from product_manager import ProductManager

#kreirana instanca
manager = ProductManager()

#spisak proizvoda
pr1 = Product("Monitor", 25000, 5)
pr2 = Product("Mobilni", 15000, 15)
pr3 = Product("Racunar", 45000, 20)
pr4 = Product("Laptop", 85000, 10)

#dodavanje proizvoda
manager.dodavanje_proizvoda(pr1)
manager.dodavanje_proizvoda(pr2)
manager.dodavanje_proizvoda(pr3)
manager.dodavanje_proizvoda(pr4)