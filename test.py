import pandas as pd

data = pd.read_csv('user_info.csv')
user_ids = set()
for i in data['user_id']:
    user_ids.add(i)
print(len(user_ids))
