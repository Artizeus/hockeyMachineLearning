import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from bioinfokit.analys import stat

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

pmDiff = []
for x, y in zip(statData['PIM'], statData['OppPIM']):
    pmDiff.append(y-x)

statData = statData.assign(PIMDiff = pmDiff)
#print(statData)
res = stat()
res.anova_stat(df=statData, res_var='G', anova_model='G ~ C(PIMDiff)')
print(res.anova_summary)

w, pvalue = stats.shapiro((ols('G ~ C(PIMDiff)', data=statData).fit()).resid)
print(w, pvalue)

#sm.qqplot(res.anova_std_residuals, line='45')
#plt.show()

#plt.scatter(pmDiff, statData["G"])
#plt.show()
def find_outliers_IQR(df):

   q1=df.quantile(0.25)

   q3=df.quantile(0.75)

   IQR=q3-q1

   outliers = df[((df<(q1-1.5*IQR)) | (df>(q3+1.5*IQR)))]

   return outliers

#print (statData)