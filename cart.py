from product import Product

class Cart:
#lista proizvoda u korpi
    def __init__(self):
        self.cart_items = []

#dodavanje proizvoda u korpu        
    def dodaj_u_korpu(self, product):
        self.cart_items.append(product)

#racunanje ukupne vrednosti korpe tj. iznosa za naplatu        
    def ukupna_vrednost(self):
        ukupno = sum(u.price * u.quantity for u in self.cart_items)
        print(f"Ukupna vrednos robe u korpi je: {ukupno} din")

#prikaz sadrzaja korpe        
    def prikaz_korpe(self):
        for product in self.cart_items:
            product.prikaz_proizvoda()