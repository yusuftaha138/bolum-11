#Faktöriyel fonksiyonu oluşturunuz ve fonksiyona gelen değer için  hata mesajları verin.

# def faktoriyel(n):
#     n = int(n)

#     if n < 0:
#         raise ValueError("Negatif sayıların faktöriyeli hesaplanamaz.")

#     sonuc = 1

#     for i in range(1, n + 1):
#         sonuc *= i
#     return sonuc

# for i in [3,6,7,'2a', -1, -7, 9]:
#     try:
#         x = faktoriyel(i)
#     except ValueError as e:
#         print(e)
#         continue
#     else:
#         print(x)

# 2- Girilen parola içinde Türkçe karakter hatası verin.

def parola_kontrol(parola):
    turkce_karakterler = "çğıöşüÇĞİÖŞÜ"
    for ch in parola:
        if ch in turkce_karakterler:
            raise ValueError("Parola Türkçe karakter içeremez.")

try:
    parola = input("Parola giriniz: ")
    parola_kontrol(parola)
except ValueError as e:
    print(e)
else:
    print("Geçerli parola.")
            