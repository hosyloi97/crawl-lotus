import pandas as pd
import csv

df = pd.read_csv("csv/follow_relationship.csv")
follow_f = open('csv/follow_relationship_.csv', 'w')
_writer_follow_f = csv.writer(follow_f)
for _row in df.itertuples():
    _writer_follow_f.writerow([_row.user_id, _row.follower_id, _row.weight])
