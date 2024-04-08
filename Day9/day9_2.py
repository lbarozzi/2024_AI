import numpy as np
import pandas as pd
import matplotlib.pylab as ply
import seaborn as sns


df = pd.read_csv("dataset/hour.csv")

df1 = df.drop(["instant", "yr", "dteday", ],axis=1)

print(df.info() )

print(df1.describe() )

print(df1.corr() ) 

print(df1.apply(lambda x: len(x.unique() )))
# 
print(df1.isnull().sum() )

X= df1.drop(["casual","registered", "cnt","atemp", "windspeed"],axis=1) # atemp correla = a temp e windspeed correla 0.093234
y = df1["cnt"]

# print (X.head() )
# print(y.head() )
from sklearn.model_selection import train_test_split
X_tr, X_t, y_tr,y_t = train_test_split(X.values,y.values,test_size=.20, random_state=42)

from sklearn.linear_model import LinearRegression, Ridge,HuberRegressor,ElasticNetCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

cl={}
cl["lin"] = LinearRegression()
cl["Ridge"] = Ridge()
cl["Huber"] = HuberRegressor()
cl["Elan"] = ElasticNetCV()
cl["Dtre"] = DecisionTreeRegressor()
cl["forrest"] = RandomForestRegressor()
cl["GBoost"] = GradientBoostingRegressor()

for k,v in cl.items():
    v.fit(X_tr, y_tr)

from sklearn.metrics import r2_score
# r2= r2_score(y_predict,y_t)

y_p= {}
r2_ = {}
for k,v in cl.items():
    print(f"testing {k}")
    y[k] = v.predict(X_t)
    r2_[k] = r2_score(y_t, y[k])
    print(r2_[k])

# show data
'''
for k,v in cl.items():
    print(f"{k}: {r2_[k]} r2")
# '''


