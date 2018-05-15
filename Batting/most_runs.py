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
    barGraph(df)

def barGraph(df):
    y_pos=np.arange(10)
    plt.bar(y_pos, df['Runs'], color=(0.2, 0.4, 0.6, 0.6))
    plt.xticks(y_pos, df['Player'])
    # Add title and axis names
    plt.title('Most Runs')
    plt.xlabel('Player')
    plt.ylabel('Runs')
    plt.show()

    
