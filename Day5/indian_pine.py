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
from sklearn.linear_model import Perceptron, LogisticRegression

cl={}

cl["Perceptron"] = Perceptron()
cl["Logistic"] = LogisticRegression()
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
    print(f"Score= {sc[k]} for {k}")

'''
for k,s in sc.items():
    print(f"Classification for: {k}")
    print(classification_report(y_t,pr[k]))
# ''' 

# B  PyTorch
import torch 
import torch.nn as nn
import torch.nn.functional as F 

device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)
print(f"Using {device} device")

device= torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
X_train = torch.FloatTensor(X_tr)
X_test = torch.FloatTensor(X_t)
y_train = torch.LongTensor(y_tr)
y_test = torch.LongTensor(y_t)

class ANN_model(nn.Module):
    def __init__(self,input_features=8, hidden1=20,hidden2=10, hidden3=4, out_features=2):
        super().__init__()
        self.f_connected1 = nn.Linear(input_features,hidden1)
        self.f_connected2 = nn.Linear(hidden1,hidden2)
        # Add hidden3 Layer
        # self.f_connected3 = nn.Linear(hidden2, hidden3)
        # self.out = nn.Linear(hidden3,out_features)
        self.out = nn.Linear(hidden2,out_features)

    def forward(self,x):
        x = F.relu(self.f_connected1(x))
        x = F.relu(self.f_connected2(x))
        # Add
        # x = F.relu(self.f_connected3(x))
        x = self.out(x)
        return x 

# To Repeatable test 
torch.manual_seed= 42

model = ANN_model()

loss_function = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),lr=0.01)

epochs = 500
final_losses = [] 

# Train FIT
for i in range(epochs):
    # i+=1
    y_pred= model.forward(X_train)
    loss=loss_function(y_pred, y_train)
    final_losses.append(loss)
    if i%1000 ==1:
        print(f"Epoch {i} loss = {loss}")

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Test 
predictions = []
with torch.no_grad():
    for i, data in enumerate(X_test):
        y_pred = model(data)
        predictions.append(y_pred.argmax().item())
    
print("Report ANN:")
print(accuracy_score(predictions, y_test))

print(classification_report(predictions, y_test))
