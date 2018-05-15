# -*- coding: utf-8 -*-
"""
Created on Sun May 13 18:57:13 2018

@author: Manav
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def refineData(data):
    for row in data:
        player=str(row[1])
        player=player.strip()
        player=str(player.split(" ")[0][:-1]) +"\n"+ str(player.split(" ")[-1])
        row[1]=player
    return data

def showMostRuns(data):
    data = refineData(data)
    df = pd.DataFrame(data,columns=['Pos','Player','Mat','Inn', 'No','Runs','HS','AVG','BF','SR','100','50','4s','6s'],dtype=float)
    print(df)
    stackBarGraph(df)
    pieGraph(df)

def stackBarGraph(df):
    N = 10
    ind = np.arange(N)    # the x locations for the groups
    width = 0.9     # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, df['Runs'], width)
    p2 = plt.bar(ind, df['BF'], width,
             bottom=df['Runs'])

    plt.ylabel('Runs & Balls')
    plt.title('Runs by Balls Faced')
    plt.xticks(ind, df['Player'])
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ('Runs', 'Balls Faced'))

    plt.show()

def barGraph(df):
    y_pos=np.arange(10)
    plt.bar(y_pos, df['Runs'], color=(0.2, 0.4, 0.6, 0.6))
    plt.xticks(y_pos, df['Player'])
    # Add title and axis names
    plt.title('Most Runs')
    plt.xlabel('Player')
    plt.ylabel('Runs')
    plt.show()

def pieGraph(df):
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0, 0,0,0,0,0,0,0)  # explode 1st slice
        # Plot
    plt.pie(df['Runs'], explode=explode, labels=(df['Player']), colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
    plt.axis('equal')
    plt.show()
