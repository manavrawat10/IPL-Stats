# -*- coding: utf-8 -*-
"""
Created on Sun May 13 18:47:21 2018

@author: Manav
"""

from Batting.most_runs import showMostRuns
from Batting.most_runs_over import showMostRunsOver
    
def callBattingGraphs(data, value):
    if value==0:
        showMostRuns(data)
    elif value==1:
        showMostRunsOver(data)
