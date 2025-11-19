# 2- Opel
# 4-Mazda
# 5-Mercedes

# with open("markalar.txt","a", encoding="utf-8") as file:
# 	file.write("6-Bmw")
#   Dosyanın sonuna eklemek yapmak istediğinde kullanılır.

# with open ("markalar.txt", "r+", encoding="utf-8") as file:
# 	markalar = file.read()
# 	markalar ="1- Toyota\n" + markalar
# 	file.seek(0)
# 	file.write(markalar)

with open ("markalar.txt", "r+", encoding="utf-8") as file:
    markalar = file.readlines()
    markalar.insert(2,"Renault\n")
    file.seek(0)

    # for marka in markalar:
    #     file.write(marka)
    file.writelines(markalar)
	
# with open("markalar.txt","r", encoding="utf-8") as file:
# 	print(file.read())
	
