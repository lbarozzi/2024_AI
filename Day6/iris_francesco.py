import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

df = pd.read_csv(url, names=['sepal length','sepal width','petal length','petal width','target'])

print('i primi 5 campioni sono: \n')
print(df.head())
print("\nalcuni dettagli sul dataset: \n")
print(df.describe())
print("\ninformazioni sul dataset: \n")
print(df.info())
print("\nle classi presenti nel dataset sono: ")
print(df['target'].unique())

'''-----------------------------------------------------------------------------------------------------------------------
    da questa prima analisi è evidente che il dataset è composto da 150 campioni, non sono presenti campi con valori nulli
    e le feature sono tutte di tipo float64, il target è rappresentato da 3 diverse classi
-----------------------------------------------------------------------------------------------------------------------'''

setosa = df.loc[df['target'] == 'Iris-setosa'].drop('target', axis=1)
versicolor = df.loc[df['target'] == 'Iris-versicolor'].drop('target', axis=1)
virginica = df.loc[df['target'] == 'Iris-virginica'].drop('target', axis=1)
print(setosa.head())
x = ['sepal length', 'sepal width', 'petal length', 'petal width']

# visualizzazione dei dati
plt.subplot(3, 1, 1)
plt.bar(x, setosa.mean(), color='r', label='setosa')
plt.ylabel('media')
plt.title('setosa')
plt.ylim(0, 8)

plt.subplot(3, 1, 2)
plt.bar(x, versicolor.mean(), color='g', label='versicolor')
plt.ylabel('media')
plt.title('versicolor')
plt.ylim(0, 8)

plt.subplot(3, 1, 3)
plt.bar(x, virginica.mean(), color='b', label='virginica')
plt.ylabel('media')
plt.title('virginica')
plt.ylim(0, 8)

plt.show()
'''-----------------------------------------------------------------------------------------------------------------------
    da questa analisi è possibile visualizzare le differenze inter-classe per le diverse feature presenti nel dataset
    ed i rapporti che intercorrono tra di esse
-----------------------------------------------------------------------------------------------------------------------'''


# visualizzazione delle diverse feature per le diverse classi
sepal_length = [df.loc[df['target'] == i]['sepal length'].mean() for i in df['target'].unique()]
sepal_width = [df.loc[df['target'] == i]['sepal width'].mean() for i in df['target'].unique()]
petal_length = [df.loc[df['target'] == i]['petal length'].mean() for i in df['target'].unique()]
petal_width = [df.loc[df['target'] == i]['petal width'].mean() for i in df['target'].unique()]

x = df['target'].unique()

plt.subplot(2, 2, 1)
plt.bar(x, sepal_length)
plt.xlabel('target')
plt.ylabel('sepal length')
plt.title('sepal length')
plt.ylim(0, 8)

plt.subplot(2, 2, 2)
plt.bar(x, sepal_width)
plt.xlabel('target')
plt.ylabel('sepal width')
plt.title('sepal width')
plt.ylim(0, 8)

plt.subplot(2, 2, 3)
plt.bar(x, petal_length)
plt.xlabel('target')
plt.ylabel('petal length')
plt.title('petal length')
plt.ylim(0, 8)

plt.subplot(2, 2, 4)
plt.bar(x, petal_width)
plt.xlabel('target')
plt.ylabel('petal width')
plt.title('petal width')
plt.ylim(0, 8)

plt.tight_layout()
plt.show()
'''-----------------------------------------------------------------------------------------------------------------------
    da questa analisi è possibile paragonare le diverse feature per le diverse classi presenti nel dataset, notando quindi
    le differenze intra-classe per le diverse feature
-----------------------------------------------------------------------------------------------------------------------'''