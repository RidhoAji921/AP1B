ulang = True
while ulang:
    sisi = int(input("masukkan sisi\t: "))
    luas = sisi*sisi
    print("luas bujur sangkar = ", luas)
    menu = int(input("1 Untuk ulang\n2 Untuk selesai\n"))
    if menu == 1:
        ulang = True
    else:
        ulang = False
