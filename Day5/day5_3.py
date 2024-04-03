import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

foo = {
    'cars' : [ "BMW","Ferrari","FIAT"],
    'pass'  : [3, 7 ,5 ]
}

df = pd.DataFrame(foo)

print(df )

df = pd.read_csv("titanic_dataset.csv", )

print(df.head(7) )
# print(df.tail() )

print(df.loc[[2,4]])
# print(df["Pclass"])
print(df.info() )

print(df.isnull().any() )
# Try 1 
clean = df.dropna()
print(clean.info())
# PREPROCESS
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Cabin"].fillna("-",inplace=True)
df["Embarked"].fillna("U",inplace=True)

# bar= df.drop(['PassengerId','Name'], axis=1,inplace=False)
# bar= df.drop(df.columns[[0,3]], axis=1,inplace=False)
# print(bar.info() )
df.drop('PassengerId',axis=1,inplace=True)

print(df.info())
# print (df["Embarked"].drop_duplicates())
print(df.index)
print(df.columns)

print(f"Age {df['Age'].mean()} +/- {df['Age'].std()} " )

print(df.head())
print(df.corr(numeric_only=True) )

df["AgeType"] = df["Sex"]

print(df.head(5)) 

#AgeType  => SIR Male > 16 anni, LADY Female > 16 anni, BOY Male <= 16, GIRL Female <=16
m_male = df["Sex"] == "male"
m_female = df["Sex"] == "female"
m_jung = df["Age"] < 17
m_old = df["Age"] > 16

#
df.loc[m_male,"AgeType"] ='SIR'
df.loc[m_female,"AgeType"] ='LADY'
df.loc[m_male & m_jung,"AgeType"] ='BOY'
df.loc[m_female & m_jung,"AgeType"] ='GIRL'

print(df["AgeType"].unique() )
print(df.head(10)[['Age','Sex','AgeType']])

m_survived = df["Survived"] == 1 

# print(m_survived)

plt.subplot(2,2,1)
x=df[m_male & m_jung]
x1=x[(x["Survived"]==1)]
plt.bar(1,x.count(),color="navy" )
plt.bar(2,x1.count(),color="green" )
for c in range(1,6):
    f=x1["Pclass"]==c
    x2=x1[f]
    plt.bar(c+3,x2.count())
    
plt.title("Jung Male")

plt.subplot(2,2,2)
x=df[m_male & m_old]
x1=x[(x["Survived"]==1)]
plt.bar(1,x.count(),color="navy" )
plt.bar(2,x1.count(),color="green" )
for c in range(1,6):
    f=x1["Pclass"]==c
    x2=x1[f]
    plt.bar(c+3,x2.count())
plt.title("Old Male")

plt.subplot(2,2,3)
x=df[m_female & m_jung]
x1=x[(x["Survived"]==1)]
plt.bar(1,x.count(),color="navy" )
plt.bar(2,x1.count(),color="green" )
for c in range(1,6):
    f=x1["Pclass"]==c
    x2=x1[f]
    plt.bar(c+3,x2.count())
plt.title("Jung Female")

plt.subplot(2,2,4)
x=df[m_female & m_old]
x1=x[(x["Survived"]==1)]
plt.bar(1,x.count(),color="navy" )
plt.bar(2,x1.count(),color="green" )
for c in range(1,6):
    f=x1["Pclass"]==c
    x2=x1[f]
    plt.bar(c+3,x2.count())
plt.title("Old Female")


# plt.show()

m_dead = df["Survived"]==0

print(len(df[m_female & m_jung & m_survived & (df["Pclass"]==2)]) )