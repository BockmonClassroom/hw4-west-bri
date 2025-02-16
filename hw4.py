#2/16/2025 Brian West
import numpy
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
rawIris = pd.read_csv("data/Iris.csv")

normalIris = rawIris
standardIris = rawIris

for i in range(4):
    normalIris.iloc[:,i] = (normalIris.iloc[:,i] - normalIris.iloc[:,i].min())/ (normalIris.iloc[:,i].max() - normalIris.iloc[:,i].min())

normalIris.to_csv('data/normal_iris.csv',index = False)


for i in range(4):
    standardIris.iloc[:,i] = (standardIris.iloc[:,i] - standardIris.iloc[:,i].mean()) / (standardIris.iloc[:,i].std())
standardIris.to_csv('data/standard_iris.csv', index = False)


    
