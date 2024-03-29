'''
Created on Sep. 20, 2023

@author: 12265
'''
from ScoreBoard import Scoreboard
from GameEntry import GameEntry

SC=Scoreboard()

score_1= GameEntry("Ali",80)
score_2= GameEntry("John",75)
score_3= GameEntry("Yash",90)
score_4= GameEntry("Elena",80)
score_5= GameEntry("Amna",60)

score_list=[score_1, score_2,score_3,score_4,score_5]
for k in score_list:
    SC.add(k)
    
print(SC)
print("****************")
print(SC[0])