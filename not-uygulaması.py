# Not Uygulaması

# 1- Menu
    # 1- Not gir
    # 2- Ortalama (90-100 -> AA , 85-59 -> BA)
    # 3- Notları Kayıt et 
    # 4- Çıkış

def not_gir():
    ad=input("Öğrenci adı:")
    soyad=input("Öğrenci soyadı:")
    not1=input("Not 1:")
    not2=input("Not 2:")
    not3=input("Not 3:")

    with open("sinav_notlari.txt","a", encoding="utf-8") as file:
        file.write(ad + " " + soyad + ":" + not1 + "," + not2 + "," + not3 + "\n")

 

def notlari_oku():
    with open("sinav_notlari.txt","r", encoding="utf-8") as file:
        for satir in file:
            print(satir)

def notlari_kaydet():
    pass
    
while True:
    islem = input("1- Not gir\n2-Notlarıoku\n3-Notları Kayıt et\n4-Çıkış\n")
    if islem =="1":
        not_gir()
    elif islem =="2":
        notlari_oku()
    elif islem =="":
        notlari_kaydet()
    else:
        break
   
