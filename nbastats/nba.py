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