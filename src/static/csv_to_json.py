import pandas as pd
import sys
import json


EMBED_TEMPLATE = (
    '<iframe width="100%" height="360px" src="https://www.youtube.com/embed/{identifier}?start={start_time}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
)


def to_left_handed(position):
    if "L" in position:
        return position.replace("L", "R")
    else:
        return position.replace("R", "L")


def get_iframes(row):
    iframes = []
    if not pd.isna(row.v1):
        link_1 = EMBED_TEMPLATE.format(
            identifier=row.v1, start_time=int(row.v1_start)
        )
        iframes.append(link_1)
    if not pd.isna(row.v2):
        link_2 = EMBED_TEMPLATE.format(
            identifier=row.v2, start_time=int(row.v2_start)
        )
        iframes.append(link_2)
    if not pd.isna(row.v3):
        link_3 = EMBED_TEMPLATE.format(
            identifier=row.v3, start_time=int(row.v3_start)
        )
        iframes.append(link_3)
    return iframes


csv_path = f"{sys.path[0]}/deceptions.csv"
data_right = {"deceptions": []}
data_left = {"deceptions": []}

df = pd.read_csv(csv_path)
for row in df.itertuples():
    iframes = get_iframes(row)

    data_right["deceptions"].append(
        {
            "id": row.Index + 1,
            "name": row.name,
            "fromPosition": row.player_position,
            "expectedPosition": row.expected_position,
            "actualPosition": row.actual_position,
            "category": row.category,
            "grip": row.grip,
            "links": iframes,
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
            "links": iframes,
            "tutorialLink": row.tutorial_link if not pd.isna(row.tutorial_link) else None,
        }
    )

with open(f"{sys.path[0]}/deceptionDataRight.json", "w") as f_right:
    json.dump(data_right, f_right)

with open(f"{sys.path[0]}/deceptionDataLeft.json", "w") as f_left:
    json.dump(data_left, f_left)
