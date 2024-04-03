import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

uri="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

df = pd.read_csv(uri, header=None, 
                 names=['Sepal Length', 'Sepal Width','Petal Length','Petal Width', 'Class Label'])

print( df.head() ) 
print( df.info() )
print( df.describe() )
print( df.corr() )
print( df["Class Label"].unique() )

#spit data/labels
y= df.iloc[0:,4].values         # Labels
X= df.iloc[0:, [0,2] ].values   #Length Data
X1= df.iloc[0:, [1,3] ].values  #Width Data
X2= df.iloc[0:, [0,1] ].values  #Sepal Data
X3= df.iloc[0:, [2,3] ].values  #Petal Data

#Plot some graph with pyplot
plt.subplot(221)

plt.scatter(X[:49,0], X[:49,1], color='red', marker='o', label='setosaa')
plt.scatter(X[50:99, 0], X[50:99, 1], color='blue', marker='o', label='vescicolosa')
plt.scatter(X[100:, 0], X[100:, 1], color='green', marker='o', label='virginica')

plt.xlabel("sepal len")
plt.ylabel("petal len")

plt.legend(loc="upper left")

plt.subplot(222)

plt.scatter(X1[:49,0], X1[:49,1], color='red', marker='o', label='setosaa')
plt.scatter(X1[50:99, 0], X1[50:99, 1], color='blue', marker='o', label='vescicolosa')
plt.scatter(X1[100:, 0], X1[100:, 1], color='green', marker='o', label='virginica')

plt.xlabel("sepal width")
plt.ylabel("petal width")

plt.subplot(223)

plt.scatter(X2[:49,0], X2[:49,1], color='red', marker='o', label='setosaa')
plt.scatter(X2[50:99, 0], X2[50:99, 1], color='blue', marker='o', label='vescicolosa')
plt.scatter(X2[100:, 0], X2[100:, 1], color='green', marker='o', label='virginica')

plt.xlabel("sepal len")
plt.ylabel("sepal width")
plt.subplot(224)

plt.scatter(X3[:49,0], X3[:49,1], color='red', marker='o', label='setosaa')
plt.scatter(X3[50:99, 0], X3[50:99, 1], color='blue', marker='o', label='vescicolosa')
plt.scatter(X3[100:, 0], X3[100:, 1], color='green', marker='o', label='virginica')

plt.xlabel("petal len")
plt.ylabel("petal width")

plt.show()

# ''' Do some graph with Seaborn
import seaborn as sns
sns.pairplot(df , hue='Class Label')

plt.show()
# '''