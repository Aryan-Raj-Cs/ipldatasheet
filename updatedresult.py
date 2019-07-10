import pandas as pd
df = pd.read_csv('matches.csv')
total_team = list(df["team1"])+ list(df["team2"])
winner=list(df["winner"])
teams = list( dict.fromkeys(total_team) )
result = {}
for team in teams:
    result[team] = {"Total_played": total_team.count(team), "won": winner.count(team),
                    "lost": total_team.count(team) - winner.count(team)}
print(result)
