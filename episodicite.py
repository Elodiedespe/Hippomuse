# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:50:25 2015

@author: edogerde
"""

"""DESCRIPTIVES ANALYSIS AND PLOTS"""

#Import systems support
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import scipy

""" VD EPISODICITE TOTALE"""
# Distribution of the variable episodicite P1 and P2
Tests =["episodicite", "when", "heure", "repereJournalier", "what", "totale" ]
Phases= ["P1", "P2"]
for test in Tests:
    for phase in Phases:
        x = df[["Test", 'Result']][(df.Test== test) & (df.Phase==phase)]
        x1 = x.dropna(subset=['Result'])
        X = x1["Result"]
        sns.kdeplot(X, shade=True, cut=0)
        sns.rugplot(X)
        plt.ylabel("Score %s en phase %s"%(test, phase))
        plt.xlabel("Age")
        plt.title("Distribution du score %s en %s" %(test, phase))


#Anova 3 way Episodicite [ score on 3] , Phase, Age, RT
Tests =["episodicite", "when", "heure", "repereJournalier", "what", "totale" ]
for test in Tests:
    Episo=df[(df.Test=='episodicite')] 
    Episo1= Episo.sort_values(by = 'Age')
    df_Episo = Episo1.dropna(subset=['Result'])

    sns.set(style="whitegrid")
    g = sns.factorplot(x="Age", y="Result", hue="RT", col="Phase", data=df_Episo,
                       palette="YlGnBu_d", size=6, aspect=.75)
    g.despine(left=True)
    plt.ylabel("Score %s"%(test))
    plt.xlabel("Age")
    
    
# Scatter Plot episodicite totale [score on 18] for P1  with mathplot
plt.plot(df_Episo.Age[df_Episo.RT == 'RT'],df_Episo.Result[df_Episo.RT == 'RT'],'o')
plt.plot(df_Episo.Age[df_Episo.RT == 'Pas RT'],df_Episo.Result[df_Episo.RT == 'Pas RT'], 'o')
plt.ylabel("Score episodicite totale en phase 2")
plt.xlabel("Age")
plt.title("Score episodicite totale en P2 en fonction de lage et du type de traitement")


# Linear regression of the score for P1 and P2 according to RT
Tests =["episodicite", "when", "heure", "repereJournalier", "what", "totale" ]
Phases= ["P1", "P2"]
for test in Tests:
    for phase in Phases:
        
        Episo=df[(df.Test=='totale') & (df.Phase== p)]
        Episo1= Episo.sort_values(by = 'Age')
        df_Episo = Episo1.dropna(subset=['Result'])
    
        sns.set(style="ticks", context="talk")
        pal = sns.cubehelix_palette(4, 1.5, .75, light=.6, dark=.2)
        g = sns.lmplot(x="Age", y="Result", hue="RT", data=df_Episo,
                       palette=pal, size=7)
        plt.ylabel("Score episodicite en phase %s"%(p))
        plt.xlabel("Age")
        plt.title("Score %s en fonction de l'âge et du type de traitement en %s" %(p))
    
# plot impact of the type of RT in RT group
Phases = ["P1", "P2"]
for p in Phases: 
    
    Episo=df[(df.Test=='episodicite') & (df.RT=='RT')& (df.Phase== p)]
    Episo1= Episo.sort_values(by = 'Age')
    df_Episo = Episo1.dropna(subset=['Result'])

    sns.set(style="ticks", context="talk")
    g = sns.lmplot(x="Age", y="Result", hue="TypeRT", data=df_Episo,
                   size=7)
    plt.ylabel("Score episodicite totale en phase %s"%(p))
    plt.xlabel("Age")
    plt.title("Score episodicite totale en fonction du type de RT en %s" %(p))
    

"""VD MUSIQUE"""

# Musique
Phases = ["P1", "P2"]
for p in Phases: 
    Episo=df[(df.Test=='musique') & (df.Item=='totale') & (df.Phase== p)] 
    Episo1= Episo.sort_values(by = 'Age')
    df_Episo = Episo1.dropna(subset=['Result'])
    sns.set(style="whitegrid")

    sns.set(style="ticks", context="talk")
    g = sns.lmplot(x="Age", y="Result", hue="ExpertiseMusicale", data=df_Episo,
               size=5)
    plt.ylabel("Score episodicite totale en phase %s"%(p))
    plt.xlabel("Age")
    plt.title("Score association odeur-musique en fonction de lexpertise musicale de l'enfant%s"%(p))

# Spearman Corr between Episodicite P1 et Episodicite P2
"""Corr = df[["Test",'Result']][(df.Test=="episodicite")]
pd.isnull(Corr)

X = Corrnan["Result"][(Corrnan.Phase=="P1")]
Y = Corrnan["Result"][(Corrnan.Phase=="P2")]
print("La correlation de spearman hedonicite %s " %(t) ) 
cor_spearman = scipy.stats.spearmanr(X, Y)"""


# Create a new column "Treatment" acording to the type of treatment RC, C, R

RC= ["sujet_001_CM", "sujet_002_AA", "sujet_005_BZ", "sujet_010_SA", 
     "sujet_011_PA", "sujet_012_OY", "sujet_017_AG", "sujet_018_FI"
     ,"sujet_024_VM"," sujet_028_CH", "sujet_029_CT"," sujet_031_GT", 
     "sujet_033_HL"]
     
C = ["sujet_003_BJ", "sujet_004_GA", "sujet_006_GM", "sujet_007_MM", 
     "sujet_008_PA", "sujet_020_AW", "sujet_021_PA", "sujet_023_CN",
     "sujet_026_AT","sujet_030_CR", "sujet_035_NA", "sujet_037_TA"]
     
R= ["sujet_009_GB","sujet_014_WS","sujet_015_NI","sujet_016_DG","sujet_022_SK",
   "sujet_027_BL","sujet_032_HB","sujet_034_HI","sujet_036_NM","sujet_038_ZH"]

# Create a empty list and fill it - Then, create a column with the value of treatment
Treatment = []
for suj in (df["sujet"]):
    if suj in RC:
        Treatment.append('RC')
    elif suj in C:
        Treatment.append('C')
    elif suj un R:
        Treatment.append('R')         
df['Traitement']= Treatment

# Create a empty column call treatment
df["Traitement"]= ""
# Fill the column
for suj in RC:
    df[df["sujet"]==suj]["Treatment"]="RC"
for suj in C:
    df[df["sujet"]==suj]["Treatment"]="C"
for suj in C:
    df[df["sujet"]==suj]["Treatment"]="R"
     
#  plots the point estimate and confidence interval
Tests =["episodicite", "when", "heure", "repereJournalier", "what", "totale" ]
Phases= ["P1", "P2"]
for test in Tests:
    for phase in Phases:
        Episo=df[(df.Test== test)& (df.Phase==phase]] 
        Episo1= Episo.sort_values(by = 'Age')
        df_Episo = Episo1.dropna(subset=['Result'])

        sns.pointplot(x="GroupeAge", y="survived", hue="Traitement", data=df_Episo);
        plt.ylabel("Score %s totale en phase %s"%(test, phase))
        plt.xlabel("Age")
        plt.title("Score %s en fonction de lexpertise musicale de l'enfant%s"%( test,phase)
        
for test in Tests:
    Episo=df[(df.Test== test)] 
    Episo1= Episo.sort_values(by = 'Age')
    df_Episo = Episo1.dropna(subset=['Result'])
    sns.set(style="whitegrid")
    g = sns.factorplot(x="Age", y="Result", hue="TypeRT", col="Phase", data=df_Episo,
                       palette="YlGnBu_d", size=6, aspect=.75)
    g.despine(left=True)
    plt.ylabel("Score %s en phase d'encodage et de recuperation"%(test))
    plt.xlabel("Age")

