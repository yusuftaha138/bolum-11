# open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu: dosyayıhangi amaçla açtığımızı belirtir.
#     "r" okuma modu   : okuma modu. belirtilen konumda dosya olmalıdır.
#     "w":(Write)yazma modu
#     ** Dosyayı konumda oluşturur. Dosya zaten varsa içeriğini siler ve yeniden ekleme yapar.
#      "a":(Append)ekleme modu. Dosya konumda yoksa oluşturur.
#      "r+":(Read and Write) okuma ve yazma modu. Dosya konumda yoksa hata verir.

with open("dosya.txt","a", encoding="utf-8") as file:
    #file.seek(0)
    (file.read(0))
    file.write("dördüncü satır\n")