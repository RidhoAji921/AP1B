def hitung_pangkat(bilangan, pangkat):
    if pangkat > 1:
        return bilangan * hitung_pangkat(bilangan, pangkat-1)
    
    return bilangan

bilangan = int(input("masukkan bilangan: "))
pangkat = int(input("masukkan pangkat: "))
hasil = hitung_pangkat(bilangan, pangkat)
print(f"hasil = {hasil}")