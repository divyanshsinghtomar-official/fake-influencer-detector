import pandas as pd

df = pd.read_csv("top_insta_influencers_data.csv")

# Renaming columns for clarity
df = df.rename(columns={
    "channel_info": "username",
    "avg_likes": "likes",
    "60_day_eng_rate": "engagement"
})

# Removing % from engagement and converting to float
df["engagement"] = df["engagement"].astype(str).str.replace("%", "")
df["engagement"] = df["engagement"].astype(float)

# Removing 'm' and 'k' from followers and converting to numeric
def convert_values(x):
    x = str(x).lower()
    if 'm' in x:
        return float(x.replace('m', '')) * 1_000_000
    elif 'k' in x:
        return float(x.replace('k', '')) * 1_000
    else:
        return float(x)

df["followers"] = df["followers"].apply(convert_values)
df["likes"] = df["likes"].apply(convert_values)

# Calculating like ratio
df["likes"] = df["likes"].astype(float)
df["like_ratio"] = df["likes"] / df["followers"]

# Implementing the logic for fake influencers
def categorize_influencer(row):
    followers = row["followers"]
    engagement = row["engagement"]
    like_ratio = row["like_ratio"]

    score = 0

    if followers > 10_000_000:
        if engagement < 0.5:
            score += 2
        elif engagement < 1.5:
            score += 1

        if like_ratio < 0.005:
            score += 2
        elif like_ratio < 0.01:
            score += 1

    elif followers > 1_000_000:
        if engagement < 0.8:
            score += 2
        elif engagement < 2.0:
            score += 1

        if like_ratio < 0.007:
            score += 2
        elif like_ratio < 0.015:
            score += 1

    elif followers > 100_000:
        if engagement < 1.5:
            score += 2
        elif engagement < 3.0:
            score += 1

        if like_ratio < 0.01:
            score += 2
        elif like_ratio < 0.02:
            score += 1

    else:
        if engagement < 2.5:
            score += 2
        elif engagement < 5.0:
            score += 1

        if like_ratio < 0.015:
            score += 2
        elif like_ratio < 0.03:
            score += 1

    if score >= 4:
        return "Fake Influencer"
    elif score >= 2:
        return "Suspicious Influencer"
    else:
        return "Genuine Influencer"
    
df["influencer_type"] = df.apply(categorize_influencer, axis=1)
print(df[["influencer_type", "username"]].head())