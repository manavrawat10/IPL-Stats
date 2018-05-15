# -*- coding: utf-8 -*-
"""
Created on Sat May 12 12:53:42 2018

@author: Manav
"""

import tkinter as tk
from stats import getData
from Batting.batting_graphs_controller import callBattingGraphs
from Bowling.bowling_graphs_controller import callBowlingGraphs

root = tk.Tk()
v = tk.IntVar()
#v.set(0)  # initializing the choice, i.e. Python
year="2018"     #bydefault 2018 year
batting_stats = ["Most Runs", "Most Runs (Over)", "Most Fours", "Most Fours (Inning)", "Most Sixes", "Most Sixes (Inning)", "Most Fifties", 
                 "Most Centuries", "Highest Score", "Best Batting Strike Rate", "Best Batting Average", "Biggest Six", "Fastest Fifties", "Fastest Centuries"]
batting_urls = ["most-runs", "most-runs-over", "most-fours", "most-fours-innings", "most-sixes", "most-sixes-innings", "most-fifties", "most-centuries",
                "highest-scores-innings", "best-batting-strike-rate", "best-batting-average", "biggest-sixes", "fastest-fifties", "fastest-centuries"]

bowling_stats = ["Most Wickets", "Most Maidens", "Most Dot Balls", "Most Dot Balls (Inning)", "Best Bowling Average", "Best Bowling Economy", "Best Bowling Economy (Inning)", 
                 "Best Bowling Strike Rate", "Best Bowling Strike Rate (Inning)", "Best Bowling (Inning)", "Most Run Conceded Innings", "Fastest Ball", "Most Hat Tricks", "Player Points"]
bowling_urls = ["most-wickets", "most-maidens", "most-dot-balls", "most-dot-balls-innings", "best-bowling-average", "best-bowling-economy", "best-bowling-economy-innings",
                "best-bowling-strike-rate","best-bowling-strike-rate-innings", "best-bowling-innings", "most-runs-conceded-innings", "fastest-balls", "most-hat-tricks", "player-points"]

def UseBatChoice():
    selected=batting_urls[v.get()]
    print(selected)
    data=getData(year,selected)
    callBattingGraphs(data, v.get())
    
def UseBowlChoice():
    selected=bowling_urls[v.get()]
    print(selected)
    data=getData(year,selected)
    callBowlingGraphs(data, v.get())
    
def year2018():
    global year
    year="2018"
def year2017():
    print("2017")
    global year
    year="2017"
def year2016():
    print("2016")
    global year
    year="2016"
def batting():
    print("Batting Stats")
    tk.Label(root, 
         text="Select the Batting Stats:",
         justify = tk.LEFT,
         padx = 20).pack()
    for val, bat in enumerate(batting_stats):
        tk.Radiobutton(root, 
                  text=bat,
                  padx = 20, 
                  variable=v, 
                  command=UseBatChoice,
                  value=val).pack(anchor=tk.W)
    root.mainloop()

def bowling():
    print("Bowling Stats")
    tk.Label(root, 
         text="Select the Bowling Stats:",
         justify = tk.LEFT,
         padx = 20).pack()
    for val, bowl in enumerate(bowling_stats):
        tk.Radiobutton(root, 
                  text=bowl,
                  padx = 20, 
                  variable=v, 
                  command=UseBowlChoice,
                  value=val).pack(anchor=tk.W)
    #root.mainloop()
mbutton = tk.Menubutton(root, text='Year')     # the pull-down stands alone
picks   = tk.Menu(mbutton)               
mbutton.config(menu=picks)           
picks.add_command(label='2018',  command=year2018)
picks.add_command(label='2017',  command=year2017)
picks.add_command(label='2016', command=year2016)
mbutton.pack()
mbutton.config(bg='white', bd=4, relief=tk.RAISED)
mbutton = tk.Menubutton(root, text='Option')     # the pull-down stands alone
picks   = tk.Menu(mbutton)               
mbutton.config(menu=picks)           
picks.add_command(label='Batting',  command=batting)
picks.add_command(label='Bowling',  command=bowling)
mbutton.pack()
mbutton.config(bg='white', bd=4, relief=tk.RAISED)
root.mainloop()
