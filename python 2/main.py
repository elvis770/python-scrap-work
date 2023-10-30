import pandas as pd

df=pd.read_json(r'/Users/elvisechefu/Desktop/python 2/data.json')

pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns

print(df)