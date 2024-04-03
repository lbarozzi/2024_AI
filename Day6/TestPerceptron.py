import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

uri="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

df = pd.read_csv(uri, header=None, 
                 names=['Sepal Length', 'Sepal Width','Petal Length','Petal Width', 'Class Label'])

print(df['Class Label'].unique())

''' Self made Perceptron
setosa = df["Class Label"]=='Iris-setosa'
vesicolor = df["Class Label"]=='Iris-versicolor'
virginica = df["Class Label"]=='Iris-virginica'

iris = {"setosa":1,"versicolor":2,"virignica":3}

# df.loc[m_male,"AgeType"] ='SIR'
df.loc[setosa,"ClassId"] = 1
df.loc[vesicolor,"ClassId"] = 2
df.loc[virginica,"ClassId"] = 3

print(df.head())

y = df.iloc[:100, 5].values         #Labels
y = np.where(y==1, -1 , 1 )         # Reconding for Perpectron
X = df.iloc[:100, [0,2]].values     #Data 


# Show the trick
plt.scatter(X[:50,0], X[:50,1], color="red", marker='o',label='Setosa')
plt.scatter(X[50:,0], X[50:,1], color="blue", marker='x',label='Vescicolor')

plt.show()

#Perceptron
from Perceptron import Perceptron
ppn = Perceptron(eta=0.01,n_iter=10)
ppn.fit( X, y)

plt.plot(range(1,len(ppn.errors_)+1 ), ppn.errors_, marker='o')

plt.show()
# '''

# scikit-learn
X = df.iloc[:, 0:4 ].values
y = df.iloc[:,4].values 
#Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

# Fit
from sklearn.linear_model import Perceptron
cl = Perceptron()
cl.fit(X_train, y_train)

# Classify
p_predictions = cl.predict(X_test)

from sklearn.neighbors import KNeighborsClassifier
cl = KNeighborsClassifier(n_neighbors=5, p=2, metric="minkowski")
cl.fit(X_train,y_train)

knn_predictions = cl.predict(X_test)


from sklearn.svm import SVC
cl = SVC()
cl.fit(X_train,y_train)

svc_predictions = cl.predict(X_test)

# Test 
from sklearn.metrics import accuracy_score
print( accuracy_score(y_test,p_predictions) ) 
print( accuracy_score(y_test,knn_predictions) ) 
print( accuracy_score(y_test,svc_predictions) ) 

from sklearn.metrics import classification_report
print( classification_report(y_test, p_predictions) )
print( classification_report(y_test, knn_predictions) )
print( classification_report(y_test, svc_predictions) )
