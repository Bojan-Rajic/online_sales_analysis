#klasa sa atributima
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

#prikaz informacija o proizvodu        
    def prikaz_proizvoda(self):
        print(f"Proizvod: {self.name},\nCena: {self.price},\nKolicina: {self.quantity}.\n ")

#metoda za ažuriranje količine    
    def azuriranje_kolicine(self, new_quantity):
        self.quantity = new_quantity