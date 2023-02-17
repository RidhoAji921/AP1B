ulang = True
while ulang:
    alas = int(input("masukkan alas\t: "))
    tinggi = int(input("masukkan tinggi\t: "))
    luas = 1/2*alas*tinggi
    print("luas segitiga = ", luas, "cm")
    menu = int(input("1 Untuk ulang\n2 Untuk selesai\n"))
    if menu == 1:
        ulang = True
    else:
        ulang = False