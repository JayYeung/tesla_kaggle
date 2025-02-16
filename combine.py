import pandas as pd
from collections import Counter

# Load the CSV files
file1 = pd.read_csv("o1_baseline.csv")
file2 = pd.read_csv("o4_baseline.csv")
file3 = pd.read_csv("gemini_pro_2.0.csv")

# Merge the three files on 'id'
merged = file1.merge(file2, on="id", suffixes=("_1", "_2")).merge(file3, on="id")
merged.rename(columns={"answer": "answer_3"}, inplace=True)

# Apply majority voting
def majority_vote(row):
    votes = [row["answer_1"], row["answer_2"], row["answer_3"]]
    return Counter(votes).most_common(1)[0][0]

merged["final_answer"] = merged.apply(majority_vote, axis=1)

# Select only relevant columns
result = merged[["id", "final_answer"]]

# Save the result
result.to_csv("majority_voted_results.csv", index=False)