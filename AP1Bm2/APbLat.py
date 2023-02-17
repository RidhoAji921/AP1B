menuError = True
nama = input("Masukkan nama anda\t: ")
while menuError:
    umur = input("Masukkan umur anda\t: ")
    if umur.isnumeric() == True:
        umur = int(umur)
        if 0 > umur or umur > 200:
            print("\nMasukkan angka yang valid!")
        else:
            menuError = False
    else:
        print("\nMasukkan angka!")
print("\n============================")
print("Nama: ", nama)
print("Umur: ", umur, "Tahun")

#buatlah program python untuk menghitung luas lingkaran, luas segitiga, dan untuk bujur sangkar