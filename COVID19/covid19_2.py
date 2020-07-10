#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Vasiki Konneh

#analyzes a data file of COVID cases/deaths in the world and compresses it
# into graphs comparing deaths and cases to number of days since the first case in respective country

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

df=pd.read_csv('COVID19.csv')
df.drop(['month','day', 'geoId','countryterritoryCode', 'year'
         ], axis=1,inplace=True)#inplace=True means to update the df file
df.rename(columns={'countriesAndTerritories':'Countries', 'popData2018':'Population', 'continentExp':'Continent',
                   'cases':'Cases', 'deaths':'Deaths', 'dateRep':'Date'},inplace=True)
df['Date']=pd.to_datetime(df['Date'])
# print(df.head(10))
# print(df.describe())
df = df.fillna('NA')
# df2 = df.groupby('Countries')[['Countries', 'Cases', 'Deaths']].sum().reset_index() #also do % of pop diagonised/killed
df2 = df.groupby(['Countries', 'Date'])[['Countries', 'Date', 'Cases', 'Deaths']].sum().reset_index()
# df3 = df2[df2['Cases']>100]

print(df2)
# print(df3)
# print(df.info())

# x=np.linspace(0,10,1000)
# y=np.sin(x)
# plt.plot(x,y,'--r')
# plt.show()
countries = df2['Countries'].unique()
t = len(countries)
print(t)

for idx in range(0,len(countries)):
    C=df2[df2['Countries']==countries[idx]].reset_index()
    plt.plot(np.arange(0,len(C)),C['Cases'], color='red', label = 'Confirmded Cases')
    plt.plot(np.arange(0,len(C)),C['Deaths'], color='black', label = 'Deaths')
    plt.title(countries[idx])
    plt.ylabel('Total number of cases')
    plt.xlabel('Days since first case')
    plt.legend()
    # plt.subplot(3, 1, idx+1)
    plt.show()



# In[ ]:




