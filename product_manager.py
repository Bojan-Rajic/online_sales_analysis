from product import Product

#atribut lista
class ProductManager:
    def __init__(self):
        self.products = []

#dodavanje proizvoda    
    def dodavanje_proizvoda(self, product):
        self.products.append(product)

#prikaz proizvoda        
    def prikazi_proizvode(self):
        for product in self.products:
            product.prikaz_proizvoda()

#prikaz ukupne vrednosti svih proizvoda            
    def ukupna_vrednost(self):
        ukupno = 0
        for product in self.products:
            ukupno += product.price * product.quantity
        print(f"Ukupna vrednost svih proizvoda je: {ukupno}\n")