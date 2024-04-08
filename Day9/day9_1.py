import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


df = pd.read_csv("Students.csv")

print(df.head())

print(df.info())

print(df.corr() ) 

# TODO: Plot some graph PSE

X= df.iloc[:,:-1]   # until mark
y= df.iloc[:,-1:]   # Mark! 

from sklearn.model_selection import train_test_split
X_tr,X_t,y_tr,y_t = train_test_split(X,y,test_size=.20, random_state=42) 
# Why 42?

from sklearn.linear_model import LinearRegression
model = LinearRegression()

model.fit(X_tr,y_tr) # Addestramento

y_predict= model.predict(X_t)

#Warna!! 
mio_tst= model.predict( [[6,2]]) # 

print(f"Predict [[6,2]]= {mio_tst}")

from sklearn.metrics import r2_score
r2= r2_score(y_predict,y_t)
print(f"R2_score: {r2}")



