'''
Write a python script that generates a bar plot with proper labels and legends that show three bars:
    – The first bar represents the total count of games Teddy played during the age 20-29
    – The second bar represents the total count of games Teddy played during the age 30-39
    – The third bar represents the total count of games Teddy played during the age 40-49
'''

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('TeddyBallgame.csv')

games_20_29 = df[(df['Age'] > 19) & (df['Age'] < 30)]['GamesPlayed'].sum()
games_30_39 = df[(df['Age'] > 29) & (df['Age'] < 40)]['GamesPlayed'].sum()
games_40_49 = df[(df['Age'] > 39) & (df['Age'] < 50)]['GamesPlayed'].sum()

age_groups = ['20-29', '30-39', '40-49']
games_played = [games_20_29, games_30_39, games_40_49]

plt.bar(age_groups, games_played, color=['blue', 'orange', 'green'])

plt.xlabel('Age Groups')
plt.ylabel('Total Games Played')
plt.title('Total Games Played by Age Group')
plt.legend(['Games Played'], loc='upper right')

plt.show()
