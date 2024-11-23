import pandas as pd
df = pd.read_csv('TeddyBallgame.csv')

# CREATING NEW COLUMNS
df['GamesPlayedPercentage'] = df['GamesPlayed'] / df['GamesPlayed'].sum()
df['GamesPlayedPercentage'] = df['GamesPlayedPercentage'] * 100
df['GamesPlayedPercentage'] = round(df['GamesPlayedPercentage'], 2)

print(df.head(5))
print(df.columns)

# ANOTHER WAY OF CREATING COLUMNS
def convert(a):
  if a < 25:
    return 'D'
  elif a < 50:
    return 'C'
  elif a < 100:
    return 'B'
  else:
    return 'A'

df['letter'] = df['GamesPlayed'].apply(convert)
df.to_csv('newData.csv') # Write dataframe to a CSV file


# DATA FILTERING 
df1 = df[df['GamesPlayed'] < 100]
  print(df1)
df2 = df[df['Age'].isin([27,30,35])]
  print(df2)
