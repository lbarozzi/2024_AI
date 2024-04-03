#indien
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

uri = "https://raw.githubusercontent.com/npradaschnor/Pima-Indians-Diabetes-Dataset/master/diabetes.csv"

df = pd.read_csv(uri)

# print(df.describe().T)

# print(df.corr() )


ddc = df.copy(deep = True)
ddc[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = ddc[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)

print(ddc.isnull().sum())

ddc.dropna(inplace=True)

from sklearn.preprocessing import StandardScaler
scaler= StandardScaler()
# print(df.head())
df_scaled = pd.DataFrame(scaler.fit_transform(ddc.copy().drop(["Outcome"],axis = 1),),
        columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age'])


# print(df_scaled.head())


from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

cl={}

cl["Knn1"]= KNeighborsClassifier(11)
cl["SVC"]=SVC()
cl["Knn2"]= KNeighborsClassifier(n_neighbors = 8, metric='minkowski')
cl["tree"]= tree.DecisionTreeClassifier(criterion='gini')
cl["RForest"] = RandomForestClassifier(n_estimators=100,criterion='gini',bootstrap=False)
cl["DeciTr"] = DecisionTreeClassifier()

y= ddc.loc[:,'Outcome'].values
# X= df.iloc[:,0:9].values
X = df_scaled.values

from sklearn.model_selection import train_test_split
X_tr, X_t, y_tr, y_t = train_test_split(X,y,test_size=0.2,random_state=42)

pr={}
for k,c in cl.items():
    c.fit(X_tr,y_tr)
    pr[k]=c.predict(X_t)


from sklearn.metrics import accuracy_score, classification_report
sc= {} 
for k,c in cl.items():
    sc[k]=accuracy_score(y_t,pr[k]) 

for k,s in sc.items():
    print(f"Score= {s} for {k}")

for k,s in sc.items():
    print(f"Classification for: {k}")
    print(classification_report(y_t,pr[k]))


