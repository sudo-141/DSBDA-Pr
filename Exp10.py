import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
iris = sns.load_dataset('iris')

# Histogram for each feature

iris.hist(figsize=(10,8))
plt.suptitle('Histograms of Iris Features')
plt.show()

#Boxplot Here

plt.figure(figsize=(10,6))
sns.boxplot(data=iris)
plt.title('Boxplot of Iris Features')
plt.show()

#Features and Types

print(iris.dtypes)
