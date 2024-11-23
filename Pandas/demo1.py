import pandas as pd

df = pd.read_csv('TeddyBallgame.csv')

print(df.loc[0]) # print row 0
print(df.loc[0:4]) # print rows 0-4
print(df['Year']) # print the column labeled 'Year'
print(df[['Age','HomeRuns']]) # print two columns
print(df['Age'][0]) # print the first row in ‘Age'
print(df[['Age','HomeRuns']][0:9]) #rows 0-9 in the given columns
