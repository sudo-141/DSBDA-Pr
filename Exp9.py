import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('train_and_test2.csv')
titanic.columns = titanic.columns.str.strip().str.lower()
titanic = titanic.rename(columns={'2urvived': 'survived'})
titanic = titanic.dropna(subset=['age'])


plt.figure(figsize=(8,6))
sns.boxplot(x='sex', y='age', hue='survived', data=titanic)

plt.title('Age Distribution by Gender and Survival')
plt.xlabel('Gender')
plt.ylabel('Age')

plt.show()
