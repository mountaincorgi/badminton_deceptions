import pandas as pd
import sys
import json

def to_left_handed(position):
    if "L" in position:
        return position.replace("L", "R")
    else:
        return position.replace("R", "L")

csv_path = f"{sys.path[0]}/deceptions.csv"
data_right = {"deceptions": []}
data_left = {"deceptions": []}

df = pd.read_csv(csv_path)
for row in df.itertuples():
    data_right["deceptions"].append(
        {
            "id": row.Index + 1,
            "name": row.name,
            "fromPosition": row.player_position,
            "expectedPosition": row.expected_position,
            "actualPosition": row.actual_position,
            "category": row.category,
            "grip": row.grip,
            "links": [l for l in row.links.split(",")] if not pd.isna(row.links) else None,
            "tutorialLink": row.tutorial_link if not pd.isna(row.tutorial_link) else None,
        }
    )
    data_left["deceptions"].append(
        {
            "id": row.Index + 1,
            "name": row.name,
            "fromPosition": to_left_handed(row.player_position),
            "expectedPosition": to_left_handed(row.expected_position),
            "actualPosition": to_left_handed(row.actual_position),
            "category": row.category,
            "grip": row.grip,
            "links": [l for l in row.links.split(",")] if not pd.isna(row.links) else None,
            "tutorialLink": row.tutorial_link if not pd.isna(row.tutorial_link) else None,
        }
    )

with open("deceptionDataRight.json", "w") as f_right:
    json.dump(data_right, f_right)

with open("deceptionDataLeft.json", "w") as f_left:
    json.dump(data_left, f_left)
