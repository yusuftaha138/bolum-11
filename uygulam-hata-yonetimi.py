liste = ["1","3","5","20b","abc","10a","60"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz.

# SORU 1 BENİM YAZDIĞIM:
# a = []
# for i in liste:
#     try:
#         a.append(int(i))
#     except ValueError:
#         pass
# print(a)

# CEVAP 1:
# for x in liste:
# try:

# print(sonuc)
# except ValueError:
# continue


# # 2: Kullanıcı 'quit (q)' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata
# mesajı yazın.

# SORU 2 BENİM YAZDIĞIM:

# while True:
#     sayi = input("Sayı giriniz (çıkmak için q): ")
#     if sayi.lower() == 'q':
#         break
#     try:
#         sayi = int(sayi)
#         print(f"Girdiğiniz sayı: {sayi}")
#     except ValueError:
#         print("Lütfen geçerli bir sayı giriniz!")
# CEVAP 2:
# while True:
#     sayi = input("sayı: ")
#     if (sayi == "q"):
#         break

#     try:
#         sonuc = float(sayi)
#         print(f"girilen sayı: {sonuc}")
#         break
#     except ValueError:
#         print("geçersiz sayı")
#     continue
# 3: Dictionary ve key bilgilerini parametre olarak alan get(dict, key) fonksiyonu hazırlayınız.

urun = {"urunAdi":"samsung s10"}

# d["fiyat"] => KeyError
# get(urun, "fiyat") => None
# get(urun, "urunAdi") => samsung S20

def get(dict, key):
    try:
        return dict[key]
    except KeyError:
        return None
print(get(urun, "fiyat"))
print(get(urun, "urunAdi")) 