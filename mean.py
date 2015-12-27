# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 10:01:11 2015

@author: edogerde
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("/home/edogerde/Desktop/mean.csv")

std = np.array(df["std"])
mean = np.array(df["mean"])
xTickMarks = ["sujet 1", "sujet 2"]
# data reco
fig = plt.figure()
ax = fig.add_subplot(111)

N=2

ind=np.arange(N) 
width=0.35

## the bars
rects1 = ax.bar(ind, mean, width,
                color='blue',
                yerr= std,
                error_kw=dict(elinewidth=2,ecolor='red'))
                
# axes and labels
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(0,500)
ax.set_ylabel("moyenne de la dose en u.a au faisseau Uncine gauche ")

ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=45, fontsize=10)

df = pd.read_csv("/home/edogerde/Desktop/QI_temps.csv")
"""Episo=df[(df.Test== test)] 
    Episo1= Episo.sort_values(by = 'Age')
    df_Episo = Episo1.dropna(subset=['Result'])
    sns.set(style="whitegrid")
    g = sns.factorplot(x="GroupeAge", y="Result", hue="TypeHedonicite", col="Phase", data=df_Episo,
                       size=6, aspect=.75)
    g.despine(left=True)"""
    
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)

sns.regplot(x="Temps", y="QI", data=df)

sns.lmplot(x="Age au bilan", y="QI", hue="Traitement", data=df)
sns.lmplot(x="Nombre de bilans", y="QI", hue="Traitement", data=df)
sns.lmplot(x="Age au bilan", y="QI",col="Traitement", data=df)
sns.lmplot(x="Nombre de bilans", y="QI",col="Traitement", hue= "Nom", data=df)


g = sns.FacetGrid(df, size=4, aspect=.7)
g.map(sns.boxplot, "Nombre de bilans", "QI", "Traitement")
g.despine(left=True)
g.add_legend(title="Traitement")  

import seaborn as sns
sns.set_style("whitegrid")
ax = sns.boxplot(x="Nombre de bilans", y="QI", data=df)
ax = sns.stripplot(x="Nombre de bilans", y="QI", data=df,size=4,jitter=True, edgecolor="gray")
ax = sns.boxplot(x="Nombre de bilans", y="QI", data=df)
ax = sns.stripplot(x="Nombre de bilans", y="QI", data=df,
                   size=4, jitter=True, edgecolor="gray")

sns.barplot(x="Traitement", y="Difference entre 1er et dernier bilan", data=df)