import pandas as pd

excel_data = pd.read_excel(r"C:\Users\Ridho Aji\OneDrive\Documents\Programming\Python\APbm7\data.xlsx")
data = pd.DataFrame(excel_data, columns=['Nama', 'Kelas', 'NPM'])
print(data)
print("\n\n")
excel_datacsv = pd.read_csv(r"C:\Users\Ridho Aji\OneDrive\Documents\Programming\Python\APbm7\data.csv")
datacsv = pd.DataFrame(excel_data, columns=['Nama', 'Kelas', 'NPM'])
print(datacsv)