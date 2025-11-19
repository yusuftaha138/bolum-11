file = open("log.txt", encoding="utf-8")

print(file.read())

file.close()
try:
    with open("log.txt", encoding="utf-8") as file:
        for i in file:
            print(i, end='')
except FileNotFoundError as e:
    print("Dosya okuma hatası")



    # print(file.read(10))
    # print(file.tell())
    # print(file.read())
    # print(file.tell())



    