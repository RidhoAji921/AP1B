from pickle import TRUE


x = [1,2,3,4,5,6,7,8,9,10]
tabel = [(1,2),(2,3),(3,4),["Apple", "Pisang", "Es Buah"]]
for i in x:
    print(f"i-nya sekarang: {i}")
for j in tabel:
    print(f"j-nya sekarang: {j}\ntipe datanya: ", type(j))
    if j == tabel[3]:
        for k in tabel[3]:
            print(f"k sekarang adalah: {k}")
print(type(tabel))
print("\n\n\n\n")
LoopControl = 0;
while (LoopControl <= 50):
    LoopControl+=1
    print(f"{LoopControl}. NGGIH")
print("\n\n\n\n")
kampus = "Gunadarma"
while kampus:
    print(kampus, '')
    kampus = kampus[1:]
print("\n\n\n\n")
n = 10
while n:
    n-=1
    if n%2 != 0:
        continue
#its weird AF tho