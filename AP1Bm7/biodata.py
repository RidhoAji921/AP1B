nama = input("Nama\t: ")
umur = int(input("Umur\t: "))
alamat = input("Alamat\t: ")

teks = "Nama: {}\nUmur: {}\nAlamat: {}", format(nama, umur, alamat)

file_bio = open("biodata.txt", "w")
file_bio.write(teks)
file_bio.close()

file_bio = open("biodata.txt", "a")
teks = file_bio.read()