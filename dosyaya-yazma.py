# "w":(Write)yazma modu
#     ** Dosyayı konumda oluşturur. Dosya zaten varsa içeriğini siler.
#     ** Eğer konummda aynı dosya varsa dosyayı siler ve yenisini oluşturur.

with open("dosya.txt","w", encoding="utf-8") as file:
    file.write("Yusuf Talha Dirican\n")
    file.write("Python Programlama Dili\n")
    file.write("Dosya İşlemleri\n")

with open ("dosya.txt","r", encoding="utf-8") as file:
   for i in file :
         print(i, end='')