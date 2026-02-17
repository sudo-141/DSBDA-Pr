import pandas as pd
import numpy as np

df = pd.read_csv("iris.csv")

df.info()

df

irisSet = (df['species']== 'Iris-setosa')
print('Iris-setosa')
print(df[irisSet].describe())

irisVer = (df['species']== 'Iris-vericolor')
print('Iris-vericolor')
print(df[irisVer].describe())

irisVer = (df['species']== 'Iris-virginica')
print('Iris-vericolor')
print(df[irisVer].describe())
