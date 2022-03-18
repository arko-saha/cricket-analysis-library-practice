
# import libraries 
from cricsummary import Duranz as Y
from numpy import mat 

# call a match
match = Y('all/1299832.yaml')

# call match details
match.summary()
match.summary(team=1)
match.summary(team=2)

# plot manhattan
match.plot_manhattan()

# plot worm
match.plot_worm()

# data frame 
df, df2 = match.team1_df, match.team2_df

# export as csv

df.to_csv('Team1.csv')
df2.to_csv('Team2.csv')

