import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('IPL.csv')
df_matches = df.drop_duplicates(subset='match_id')

wins = df.groupby('match_won_by')['match_id'].nunique()
wins.sort_values(ascending=False).head(10).plot(kind='bar')
plt.title('Top 10 IPL Winning Teams')
plt.xlabel('Team')
plt.ylabel('Matches Won')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('ipl_graph1.png')
plt.close()

df_matches['toss_match_win'] = df_matches['toss_winner'] == df_matches['match_won_by']
toss_impact = df_matches['toss_match_win'].value_counts()
toss_impact.plot(kind='bar', color=['green', 'red'])
plt.title('Toss Winner = Match Winner?')
plt.xticks([0, 1], ['Haan', 'Nahi'], rotation=0)
plt.ylabel('Matches')
plt.tight_layout()
plt.savefig('ipl_graph2.png')
plt.close()

top_players = df_matches['player_of_match'].value_counts().head(10)
top_players.plot(kind='bar', color='orange')
plt.title('Top 10 Player of the Match Winners')
plt.xlabel('Player')
plt.ylabel('Times Won')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('ipl_graph3.png')
plt.close()

season_runs = df.groupby('season')['runs_total'].sum()
season_runs.plot(kind='line', marker='o', color='blue')
plt.title('IPL Season Wise Total Runs')
plt.xlabel('Season')
plt.ylabel('Total Runs')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('ipl_graph4.png')
plt.close()

top_venues = df.groupby('venue')['runs_total'].sum()
top_venues.sort_values(ascending=False).head(10).plot(kind='bar', color='purple')
plt.title('Top 10 High Scoring Venues')
plt.xlabel('Venue')
plt.ylabel('Total Runs')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('ipl_graph5.png')
plt.close()

print("Saare 5 graphs save ho gaye!")


