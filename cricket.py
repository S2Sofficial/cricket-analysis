import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #visualization
plt.rcParams['figure.figsize'] = (14, 8)
df = pd.read_csv("E:\\t20.csv")
print('------------------------------------------------------------')
print('------------------------------------------------------------')
print(df.info())
print()
print('------------------------------------------------------------')
print('------------------------------------------------------------')
print('Total Matches are::::',df['id'].max())
print()
print('------------------------------------------------------------')
print('------------------------------------------------------------')
print('How many seasons data we’ve got in the dataset?')
print(df['season'].unique())
print()
print('------------------------------------------------------------')
print('------------------------------------------------------------')
print('Which Team had won by maximum runs?')
print(df.iloc[df['win_by_runs'].idxmax()])
print()
print('------------------------------------------------------------')
print('------------------------------------------------------------')
print('Which Team had won by maximum wickets?')
print(df.iloc[df['win_by_wickets'].idxmax()]['winner'])
print()
print('------------------------------------------------------------')
print('------------------------------------------------------------')
print('Which Team had won by (closest margin) minimum runs?')
print(df.iloc[df[df['win_by_runs'].ge(1)].win_by_runs.idxmin()]
['winner'])
print()
print('------------------------------------------------------------')
print('------------------------------------------------------------')
print('Which Team had won by minimum wickets?')
print(df.iloc[df[df['win_by_wickets'].ge(1)].win_by_wickets.idxmin()])
print()
print('------------------------------------------------------------')
print('------------------------------------------------------------')
print('Which season had most number of matches?')
plt.bar(x='season',data=df,height=df['season'])
plt.show()
print()
print('------------------------------------------------------------')
print('------------------------------------------------------------')
print('The Most Successful IPL Team is:::')
data = df.winner.value_counts()
print(data)
print()
print('------------------------------------------------------------')
print('------------------------------------------------------------')
print('The Players who got maximum times Man of the Match are:::')
top_players = df.player_of_match.value_counts()[:10]
print(top_players)
print("Data Frame Analysis")
menu=''' 1. Top record of the Players
\n 2. Bottom Records of the Players
\n 3. To print particular column
\n 4. To print multiple columns
\n 5. To display complete statistics of the Matches
\n Press enter to go back '''
print(menu)
ch=int(input("Enter your choice"))
if ch==1:
n=int(input("Enter the number of records to be displayed"))
print("Top ", n," records from the dataframe")
print(df.head(n))
elif ch==2:
n=int(input("Enter the number of records to be displayed"))
print("Bottom ", n," records from the dataframe")
print(df.tail(n))
elif ch==3:
print("Name of the columns\n",df.columns)
columns\n",df.columns)
co=input("Enter the column name to be displayed")
print(df[[co]])
elif ch==4:
print("Name of the columns\n",df.columns)
co=eval(input("Enter the column names as list in square bracket"))
print(df[co])
elif ch==5:
print("The statistics of the dataframe is:", df.describe(include='all'))
