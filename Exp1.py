import pandas as pd
import numpy as np

df = pd.read_csv("swiggy.csv")
print(df)

#df.head() 
#print(df) --> To show 1st five rows

#df.tail() 
#print(df) --> To show last 5 rows

#df['Price'] = df['Price'].info() 
#print(df) #--> info about the 'Price' column dataset

#df['Price'] = df['Price'].mean() 
#print(df) --> to calculate mean of the dataset

#print(df.info()) --> To show information about dataset

#print(df.shape) --> (8680, 10) --> To show dimensions of the dataset

#print(df.isnull().sum()) --> To show missing values

#print(df.describe()) --> To show statistical view of the dataset

#df.dropna()
#print(df) --> To remve null values

#data = {'Area':[1,2,3,4],'City':['Bangalore','Bangalore','Bangalore','Bangalore',],'Restaurant':['Tandoor Hut','Kim Lee','Nh8','Tunday Kababi']}
#df = pd.DataFrame(data) 
#print(df) --> To View the dataframe 
