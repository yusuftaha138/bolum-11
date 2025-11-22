try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x / y)
except (ZeroDivisionError, ValueError) as e:
    print("x ve y sayısal değerler olmalıdır! Sıfır olamaz!")
    print(e)
except Exception as e:
    print("Beklenmedik bir hata oluştu!")
    print(e)
else:
    pass
finally:
    print("finally bşoğu çalıştı")