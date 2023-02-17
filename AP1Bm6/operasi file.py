f = open(r"C:\Users\Ridho Aji\OneDrive\Documents\Programming\Python\Apbm6\sample.txt", "r")
print(f.read()) #mencetak seluruh isi file
print("########################################")
f = open(r"C:\Users\Ridho Aji\OneDrive\Documents\Programming\Python\Apbm6\sample.txt", "r")
#perlu dideklarasikan lagi untuk menampilkan keseluruhan
print(f.read(5)) #mencetak sebagian isi file (5 huruf pertama)
print("########################################")
f = open(r"C:\Users\Ridho Aji\OneDrive\Documents\Programming\Python\Apbm6\sample.txt", "r")
print(f.readline()) #mencetak perbaris
print(f.readline())
print(f.readline())
#menutup file
f.close()