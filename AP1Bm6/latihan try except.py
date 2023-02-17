number = 2;
while number != -1:
    try:
        number = int(input("Masukkan angka: "))
    except ValueError:
        print("ITU BUKAN ANGKA!!!!!!!!!!!!!!!!!!")