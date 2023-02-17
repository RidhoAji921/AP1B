i = 1
x = int(input("Masukkan banyak baris: "))
while x:
    while (i <= x):
        print(i, end="")
        i += 1
    x -= 1
    i = 1
    print("\n")

bintang = ""
jumlahBintang = int(input("masukkan Jumlah Bintang: "))
while jumlahBintang:
    bintang += "*"
    jumlahBintang -= 1
    print(bintang)