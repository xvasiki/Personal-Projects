#!/usr/bin/env python
# coding: utf-8

#This code takes a data set from data.gov which provides quantitative information about car accidents in Maryland in 2012. 
#It manipulates the data and constructs data visualizations of some of the paramaters. This was a good introductory project for me in working more with
#different types of data viusalizations. 
#It also made me more comfortable in breaking down data in ways I best saw fit, such as counting the number of accidents for a particular parameter. 
#From trial and error I was able to discern which visuals worked best depending on the data. 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
from operator import itemgetter
from datetime import datetime
import operator
import random
import matplotlib.patches as mpatches


df=pd.read_csv("2012CarCrashes.csv")
df.drop(['ACC_TIME_CODE','ROAD', 'INTERSECT_ROAD','DIST_FROM_INTERSECT', 'CITY_NAME', 
         'DIST_DIRECTION', 'COUNTY_CODE', 'VEHICLE_COUNT', 'PROP_DEST', 
         'COLLISION_WITH_2', 'CASE_NUMBER', 'BARRACK'], axis=1,inplace=True) 
                                #--> inplace=True means to update the df file
df["ACC_DATE"]= pd.to_datetime(df["ACC_DATE"])  #-->converts datatype to datetime
df = df.sort_values('ACC_TIME') #-->sorts according to time of accident
# df.info() #--> necessary for insight into data type of each column
    
injury_count = df['INJURY'].value_counts()
acc_times = df['ACC_TIME'].value_counts()
acc_days = df['DAY_OF_WEEK'].value_counts()
acc_colls = df['COLLISION_WITH_1'].value_counts()
acc_county = df['COUNTY_NAME'].value_counts()

print(df)
#----------------------------------------#
#Pie chart of injuries v. no injuries
print(injury_count)
labels = 'Injuries', 'No Injuries'
colors = 'orange', 'green'
x=injury_count
explode = (0, 0.1)  # explode 2nd slice
plt.pie(x, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Injury Breakdown')
plt.axis('equal')
plt.show()

#----------------------------------------#
#Pie Chart breakdown of accidents per day of week
x=acc_days
print(acc_days)
labels = 'Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'
colors = 'orange', 'green', 'red', 'yellow', 'purple', 'blue', 'pink'
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  # explode all slices
plt.pie(x, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Breakdown of Accidents per Day of Week' )
plt.axis('equal')
plt.show()


#----------------------------------------#
#BAR GRAPH of different collision types
height = [10675, 4299,2205, 465,115,32,846]
bars = ('VEH','FIXED OBJ','OTHR','ANIMAL','PED','BIKE','NON_COLL')
y_pos = np.arange(len(bars))
plt.bar(y_pos, height, color=['black', 'red', 'green', 'blue', 'cyan', 'pink','yellow','purple','gray'])
# y_pos = [8]
plt.xticks(y_pos, bars)
plt.title('Types of Collisions')
plt.xlabel('Collision With')
plt.ylabel('Number of Collisions')
plt.grid(zorder=0)
plt.show()
#----------------------------------------#

#Bar graph for time of collisions vs number of collisions
height = [420,454,432,359,369,504,764,1008,976,845,682,827,913,855,1104,1247,
         1280,1427,1085,748,663,611,520,555]
bars = []
for i in range(24):
    bars.append(int(i))
y_pos = np.arange(len(bars))
plt.bar(y_pos, height, color=['black', 'red', 'green', 'blue', 'cyan', 'pink','yellow','purple','gray'])
plt.xticks(y_pos, bars)
plt.title('Number of Collisions vs. Time')
plt.xlabel('Time of Collision (24HR)')
plt.ylabel('Number of Collisions')
plt.grid(zorder=0)
plt.show()



