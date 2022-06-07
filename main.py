import numpy as np
import pandas as pd
from sklearn import linear_model

statsFile = ("hockeyStats.csv")#File with team stats
seasonFile = ("seasonResults.csv")#File with all games and results

#Creates a DataFrame object for stats with the index being the team names
statData = pd.read_csv(statsFile)
statData.set_index("Team", inplace=True)

teams = statData.index #Gets the names of teams as a list
teamData = statData.loc[teams[0]].index #Gets the name of stats as a list

#Creates a DataFrame object for games
gameData = pd.read_csv(seasonFile)


# Creates a base to compare our predictions to
# homeWins = 0
# numGames = len(gameData["G2"])
# for x in range(numGames):
#     if gameData["G2"][x] > gameData["G"][x]:
#        homeWins+=1
# print (homeWins/numGames)
# Results: Home team wins 53.66% of the time this season

#Function responsible for comparing the stats of teams in a given game
#def readGame(hTeam, aTeam, hScore, aScore):
    

print (statData)