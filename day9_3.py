import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("DCCV_BILENERG_08042024121943600.csv")

print(df.head(2))

print(df.columns)

df1= df.drop(["ITTER107", "Territorio", "TIPO_DATO4", "Tipo dato", "Disponibilità", 
              "Settore uso", "SETTORE_USO", "Seleziona periodo", "Flag Codes", "Flags"],axis=1)
print( df1.info() ) 

#plot
