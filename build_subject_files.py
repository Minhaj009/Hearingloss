import pandas as pd
from pathlib import Path

# Considering the original dataset is in the same directory
SRC = Path("EVOreal_time_synth.csv") # source paths
OUT = Path("data/subjects") # folder to store subject files

df = pd.read_csv(SRC, parse_dates=["Timestamp"])

# Group samples by ID and then sort them by Timestamp
for subject_id, group in df.groupby("ID"):
    subject_df = (
        group
        .sort_values("Timestamp")
        .reset_index(drop=True)
    )
    subject_df.insert(0, "minute_i", subject_df.index) # logged minute i
    subject_df.to_csv(OUT / f"subject_{subject_id}.csv", index=False)

print(f"Saved {df['ID'].nunique()} subject files to {OUT}/") # full recordings per participant with correct temporal order
