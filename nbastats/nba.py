import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Find the folder where this script is located
script_folder = Path(__file__).parent

# Build the full path to nba.csv
csv_file = script_folder / "nba.csv"

print("Looking for:", csv_file)
print("File exists:", csv_file.exists())

# Load dataset
df = pd.read_csv(csv_file)

print("Dataset loaded successfully!")
print(df.head())

# Top 10 scorers
top10 = df.sort_values(by="PTS", ascending=False).head(10)

print("\nTop 10 Scorers:")
print(top10[["PLAYER", "TEAM", "PTS"]])

# Top 10 rebounders
top10_reb = df.sort_values(by="REB", ascending=False).head(10)

print("\nTop 10 Rebounders:")
print(top10_reb[["PLAYER", "TEAM", "REB"]])

# Top 10 assist leaders
top10_ast = df.sort_values(by="AST", ascending=False).head(10)

print("\n Top 10 Assist Leaders:")
print(top10_ast[["PLAYER", "TEAM", "AST"]])


# Top 10 efficiency leaders
top10_efficiency = df.sort_values(by="EFF", ascending=False).head(10)

print("\nTop 10 Efficiency Leaders:")
print(top10_efficiency[["PLAYER", "TEAM", "EFF"]])


# visualize top scorers
top10_plot = df.sort_values("PTS", ascending=False).head(10)

plt.figure(figsize=(10, 5))
plt.bar(top10_plot["PLAYER"], top10_plot["PTS"], color='orange')
plt.xticks(rotation=45)
plt.title("Top 10 Scorers in NBA")
plt.ylabel("Points")
plt.tight_layout()
plt.show()

# relationship between minutes and points

plt.figure(figsize=(8, 6))
plt.scatter(df["MIN"], df["PTS"])
plt.xlabel("Minutes Played")
plt.ylabel("Points Scored")
plt.title("Minutes VS points")
plt.show()


# team analysis

team_points = df.groupby("TEAM")["PTS"].sum().sort_values(ascending=False)

print(team_points.head(10))


# graph

team_points.head(10).plot(kind='bar', figsize=(10, 5), color='green')
plt.title("Top 10 Teams by Total Points")
plt.ylabel("Total Points")
plt.show()

# points per minute
# Efficiency metric: Points per minute played

df["PTS_PER_MIN"] = df["PTS"] / df["MIN"]
leaders = df.sort_values(by="PTS_PER_MIN", ascending=False).head(10)

print(leaders [["PLAYER","TEAM", "PTS_PER_MIN"]])

# correlation matrix

numeric_cols = ["PTS","REB", "AST", "MIN", "EFF", "TOV"]
corr = df[numeric_cols].corr()

print(corr)

# visualize correlation matrix

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True)
plt.title("NBA stats correlation matrix")
plt.show()