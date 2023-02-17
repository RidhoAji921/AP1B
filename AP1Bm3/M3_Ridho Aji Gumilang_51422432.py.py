angka = int(input("masukkan angka: "))
if angka == 0:
    print("angka 0 bukanlah ganjil atau genap")
elif angka%2 == 0:
    print("angka ", angka, " adalah genap")
elif angka%2 == 1:
    print("angka ", angka, " adalah ganjil")