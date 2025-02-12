import pandas as pd

# Load the dataset
df = pd.read_csv("netflix_titles.csv")  # Adjust path if necessary
df.head()  # Displays the first 5 rows
df.info()  # Get column types and non-null counts
df.describe()  # Statistical summary of numerical columns
df.isnull().sum()  # Check for missing values in each column

# For missing values, you can either fill them or drop them:
df.dropna(inplace=True)  # Drop rows with missing values (if necessary)
df['Release Year'] = pd.to_datetime(df['Release Year'], errors='coerce').dt.year
df['Duration'] = df['Duration'].str.replace(' min', '').astype(int)
import matplotlib.pyplot as plt
import seaborn as sns

# Count genres
genre_count = df['Genre'].value_counts()

# Plotting
plt.figure(figsize=(12, 6))
sns.barplot(x=genre_count.index, y=genre_count.values, palette="viridis")
plt.xticks(rotation=90)
plt.title('Distribution of Genres')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.show()
# Plotting the release year distribution
plt.figure(figsize=(12, 6))
sns.histplot(df['Release Year'], bins=20, kde=True, color='purple')
plt.title('Distribution of Movies by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.show()
# Get top 10 countries by movie count
country_count = df['Country'].value_counts().head(10)

# Plotting
plt.figure(figsize=(12, 6))
sns.barplot(x=country_count.index, y=country_count.values, palette="Blues")
plt.xticks(rotation=45)
plt.title('Top 10 Countries by Movie Count')
plt.xlabel('Country')
plt.ylabel('Count')
plt.show()
# Plotting the ratings distribution
plt.figure(figsize=(12, 6))
sns.countplot(x='Rating', data=df, palette='magma')
plt.xticks(rotation=45)
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()
# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title('Correlation Heatmap')
plt.show()
