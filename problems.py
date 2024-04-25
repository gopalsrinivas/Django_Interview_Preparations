import pandas as pd
ds = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(ds)
print(type(ds))
print("Convert Pandas Series to Python List")
print(ds.tolist())
print(type(ds.tolist()))
