from product import Product
from product_manager import ProductManager
from cart import Cart

#kreirana instanca
manager = ProductManager()
korpa = Cart()

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

#prikaz svih proizvoda
manager.prikazi_proizvode()

#prikaz ukupne vrednosti svih proizvoda
manager.ukupna_vrednost()

#dodavanje tri artikla u korpu
korpa.dodaj_u_korpu(pr1)
korpa.dodaj_u_korpu(pr3)
korpa.dodaj_u_korpu(pr4)

#ispis sadrzaja korpe
korpa.prikaz_korpe()

#ispis ukupne vrednosti korpe
korpa.ukupna_vrednost()