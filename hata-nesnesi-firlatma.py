# print(10 / 0)

# x = 10

# if x > 5:
    # raise ValueError("x 5 den büyük olamaz.")

def renklendir(text, renk):
    renkler = ("blue","red","white","black","orange")

    if type(text) is not str:
        raise TypeError("text str tipinde olmalidır.")

    if type(renk) is not str:
        raise TypeError("renk str tipinde olmalıdır.")
    if renk not in renkler:
        raise ValueError(" geçersiz bir renk.")
    
    print(f"{renk} renkli yazı: {text}")
try:
    renklendir("selam","red")
    renklendir("merhaba","yellow")
except (TypeError, ValueError) as ex:
    print(ex)