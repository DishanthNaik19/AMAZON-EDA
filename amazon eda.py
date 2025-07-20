# -*- coding: utf-8 -*-
"""
Created on Sat Jul 19 11:00:35 2025

@author: Dishanth
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast

# Optional for better plot style
sns.set(style="whitegrid")
# Load CSVs
titles = pd.read_csv("titles.csv", encoding='latin1')
credits = pd.read_csv("credits.csv", encoding='latin1')


# Preview
print(titles.head())
print(titles.info())
print(credits.head())

# Convert from string to list
titles['genres'] = titles['genres'].fillna('[]').apply(ast.literal_eval)
titles['production_countries'] = titles['production_countries'].fillna('[]').apply(ast.literal_eval)
# Fill missing certifications with 'Unknown'
titles['age_certification'] = titles['age_certification'].fillna('Unknown')

# Fill missing scores with mean
titles['imdb_score'] = titles['imdb_score'].fillna(titles['imdb_score'].mean())
titles['imdb_votes'] = titles['imdb_votes'].fillna(0)
titles['tmdb_score'] = titles['tmdb_score'].fillna(titles['tmdb_score'].mean())
df = titles.merge(credits, on="id", how="left")
import seaborn as sns
sns.countplot(data=titles, x='type', palette='pastel')
plt.title("Content Type Distribution")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()
yearly_count = titles['release_year'].value_counts().sort_index()
plt.figure(figsize=(14, 6))
sns.lineplot(x=yearly_count.index, y=yearly_count.values, color='green')
plt.title("Content Released Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.show()
import ast

# Only convert string entries that are not already lists
titles['genres'] = titles['genres'].apply(
    lambda x: ast.literal_eval(x) if isinstance(x, str) else x
)

# Now explode and count
all_genres = titles['genres'].explode()
top_genres = all_genres.value_counts().head(10)

# Plot
plt.figure(figsize=(10,6))
sns.barplot(x=top_genres.values, y=top_genres.index, palette='coolwarm')
plt.title("Top 10 Genres on Amazon Prime")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.show()
import ast

# Only apply literal_eval if it's a string
titles['production_countries'] = titles['production_countries'].apply(
    lambda x: ast.literal_eval(x) if isinstance(x, str) else x
)

# Explode and get top countries
countries = titles['production_countries'].explode()
top_countries = countries.value_counts().head(5)

# Plot pie chart
plt.figure(figsize=(8,8))
plt.pie(top_countries, labels=top_countries.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title("Top 5 Producing Countries")
plt.axis('equal')
plt.show()
# Chart 5: Age Certification Distribution
plt.figure(figsize=(10,5))
sns.countplot(data=titles, x='age_certification', order=titles['age_certification'].value_counts().index, palette='Set2')
plt.title("Distribution of Age Certification")
plt.xlabel("Age Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.show()


# Chart 6: IMDb Score Distribution
plt.figure(figsize=(10,5))
sns.histplot(data=titles, x='imdb_score', bins=20, kde=True, color='skyblue')
plt.title("IMDb Score Distribution")
plt.xlabel("IMDb Score")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.show()


# Chart 7: Runtime Distribution
plt.figure(figsize=(10,5))
sns.histplot(data=titles, x='runtime', bins=30, color='salmon')
plt.title("Runtime Distribution of Titles")
plt.xlabel("Runtime (minutes)")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.show()


# Chart 8: TMDB Popularity Distribution
plt.figure(figsize=(10,5))
sns.histplot(data=titles, x='tmdb_popularity', bins=30, color='orange')
plt.title("TMDB Popularity Distribution")
plt.xlabel("TMDB Popularity Score")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.show()


# Chart 9: IMDb Votes Distribution
plt.figure(figsize=(10,5))
sns.histplot(titles['imdb_votes'], bins=30, color='teal')
plt.title("IMDb Votes Distribution")
plt.xlabel("Number of IMDb Votes")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.xscale('log')  # Log scale because of skewed distribution
plt.show()


# Chart 10: TMDB Score Distribution
plt.figure(figsize=(10,5))
sns.histplot(titles['tmdb_score'], bins=20, kde=True, color='violet')
plt.title("TMDB Score Distribution")
plt.xlabel("TMDB Score")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.show()


# Chart 11: Type vs IMDb Score (Box Plot)
plt.figure(figsize=(8,5))
sns.boxplot(data=titles, x='type', y='imdb_score', palette='pastel')
plt.title("IMDb Score by Content Type")
plt.xlabel("Type")
plt.ylabel("IMDb Score")
plt.show()


# Chart 12: Type vs Runtime (Box Plot)
plt.figure(figsize=(8,5))
sns.boxplot(data=titles, x='type', y='runtime', palette='muted')
plt.title("Runtime by Content Type")
plt.xlabel("Type")
plt.ylabel("Runtime (minutes)")
plt.ylim(0, 300)  # Limit extreme outliers
plt.show()


# Chart 13: IMDb Score vs Votes (Scatter Plot)
plt.figure(figsize=(10,6))
sns.scatterplot(data=titles, x='imdb_score', y='imdb_votes', alpha=0.6)
plt.title("IMDb Score vs IMDb Votes")
plt.xlabel("IMDb Score")
plt.ylabel("IMDb Votes")
plt.yscale('log')
plt.grid(True)
plt.show()


# Chart 14: IMDb Score vs Runtime (Scatter)
plt.figure(figsize=(10,6))
sns.scatterplot(data=titles, x='runtime', y='imdb_score', alpha=0.5)
plt.title("Runtime vs IMDb Score")
plt.xlabel("Runtime (minutes)")
plt.ylabel("IMDb Score")
plt.grid(True)
plt.show()


# Chart 15: Avg IMDb Score per Year
yearly_score = titles.groupby('release_year')['imdb_score'].mean()

plt.figure(figsize=(14,6))
sns.lineplot(x=yearly_score.index, y=yearly_score.values, color='navy')
plt.title("Average IMDb Score Over the Years")
plt.xlabel("Release Year")
plt.ylabel("Average IMDb Score")
plt.grid(True)
plt.show()


# Chart 16: Top Genres vs Avg IMDb Score
genre_scores = titles.explode('genres').groupby('genres')['imdb_score'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=genre_scores.values, y=genre_scores.index, palette='mako')
plt.title("Top 10 Genres by Average IMDb Score")
plt.xlabel("Average IMDb Score")
plt.ylabel("Genre")
plt.show()


# Chart 17: Correlation Heatmap of Numerical Features

# Select relevant numerical columns
num_cols = ['imdb_score', 'imdb_votes', 'tmdb_score', 'tmdb_popularity', 'runtime']

# Compute correlation matrix
corr_matrix = titles[num_cols].corr()

# Plot the heatmap
plt.figure(figsize=(10,6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap: IMDb, TMDB, Runtime, Votes")
plt.show()


sample_titles = titles[num_cols].dropna().sample(500, random_state=42)

# Plot pairplot
sns.pairplot(sample_titles, diag_kind='kde', plot_kws={'alpha': 0.6})
plt.suptitle("Pair Plot of IMDb, TMDB, Votes, Popularity, Runtime", y=1.02)
plt.show()
