# Class
class Product:
    pass
    #method
    # attiribute,property
    def __init__(self,name,price, isActive):
       self.name = name
       self.price = price
       self.isActive = isActive


# Instance- Nesne- Object
p1 = Product("İphone 15", 52000, True)
p2 = Product("iphone 13", 76000,False)
p3 = Product("xiaomi", 25000,True)

urunler = [p1, p2, p3]
for urun in urunler:
    print(f"ürün adı: {urun.name} ürün fiyatı: {urun.price} ürün aktif mi? {urun.isActive}")

print(urunler)
