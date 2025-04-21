def score_clarity(df):
    def score_row(row):
        if row["ext"] in [".md", ".txt"]:
            return "High"
        elif row["ext"] in [".py", ".json"]:
            return "Medium"
        else:
            return "Low"
    df["clarity_score"] = df.apply(score_row, axis=1)
    return df