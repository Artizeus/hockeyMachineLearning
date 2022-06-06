import numpy as np
import pandas as pd
import sklearn

statsFile = ("hockeyStats.csv")

statData = pd.read_csv(statsFile)

teams = statData["Team"]


print (statData.loc[1]["CorsiF"])