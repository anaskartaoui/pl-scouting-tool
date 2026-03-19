import pandas as pd

df = pd.read_csv("data/raw/fbref_PL_2024-25.csv", encoding = "latin-1")
df.to_csv("data/raw/fbref_PL_2024-25.csv", index=False)
print(df.head())
print(df.shape)
print(df.columns.tolist())
