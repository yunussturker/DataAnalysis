import pandas as pd 

df = pd.read_csv("GBvideos.csv")

#First 10 records
result = df.head(10)

# Second 5 records
result = df[5:20].head()

# Column names and Number of columns
result = df.columns
result = len(df.columns)

# Drop this columns and List the rest of all
df.drop(["thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description", "trending_date"], axis=1, inplace=True)
result = df.columns

# Show the likes average
result = df["likes"].mean()

# Show the dislikes average
result = df["dislikes"].mean()

# Show the first 50 title's likes and dislikes
result = df.head(50)[["title", "likes", "dislikes"]]

# Show the most viewed title's name
result = df[df["views"].max() == df["views"]]["title"].iloc[0]

# Show the lowest viewed title's name
result = df[df["views"].min() == df["views"]]["title"].iloc[0]

# Show the top 10 viewed videos
result = df.sort_values("views", ascending=False).head(10)[["title", "views"]]

# Get the average of likes sorted by category
result = df.groupby("category_id").mean().sort_values("likes")["likes"]

# Get the total of comments sorted by category
result = df.groupby("category_id").sum().sort_values("comment_count", ascending=False)["comment_count"]

# Video numbers for each category
result = df["category_id"].value_counts()

# Add a new column and show each video's title length
df["title_len"] = df["title"].apply(len)
result = df

# Add a new column and show tag numbers for each video
df["tag_count"] = df["tags"].apply(lambda x: len(x.split('|')))
result = df
 
print(result)
