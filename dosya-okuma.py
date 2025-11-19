"""
    Dosya açmak ve olutşturmak için open() fonksiyonu kullanılır.

    Kullanımı        : open(dosya_adi,dosya_erişme_modu)
    dosya_erişme_modu: dosyayı hangi amaçla açtığımızı belirtir.
    "r" okuma modu   : okuma modu. belirtilen konumda dosya olmalıdır.
    seek             : cursor konumu
"""

f= open("log.txt", encoding='utf-8')
print(f.read())