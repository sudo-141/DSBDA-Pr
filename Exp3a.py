import pandas as pd
import numpy as np

stat = {'Customer_id':[101,102,103,104,105],
        'Gender':['Male','Male','Female','Female','Female'],
        'Age':[19,21,35,45,22]}

df = pd.DataFrame(stat)
print(df)

df.info()

df.loc[:,'Age'].mean()

df.mean(axis=1)[0:2]

df.mode()

df.loc[:,'Age'].mode()

df.loc[:,'Gender'].mode()

df.min()

df.max()

df.std()

df.loc[:,'Age'].std()

df.groupby(['Gender']).Age.mean()

from sklearn import preprocessing

enc = preprocessing.OneHotEncoder()

enc_df = pd.DataFrame(enc.fit_transform(df[['Gender']]).toarray())

print(enc_df)
