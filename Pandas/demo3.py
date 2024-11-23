import matplotlib.pyplot as plt
import pandas as pd

#  SIMPLE DATA PLOTTING
df = pd.read_csv('TeddyBallgame.csv')
df.plot(kind='scatter', x='GamesPlayed', y='HomeRuns')
plt.show()
