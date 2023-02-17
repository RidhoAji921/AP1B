import pandas as pd

#pd.DataFrame
mydataset = {
  'cars': ["BMW", "Volvo", "Ford", "Honda", "Ferrari", "Lamborghini", "Toyota"],
  'passing': [3, 7, 2, 4, 3, 4, 5]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

print("\n\n\n")
#pd.Series
a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
