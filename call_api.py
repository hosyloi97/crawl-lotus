import requests
import csv
import config as config

# init value of params
import url_constant

no_page = 1
dev = 0

data = ['user_id', 'username', 'full_name', 'total_follow']
# # config for write to file csv
with open('test_csv.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(data)

    # firstly, get all my followers info
    query = {'user_id': config.my_id, 'partner_id': config.my_id, 'no_page': no_page, 'dev': dev}
    response = requests.get(url=url_constant.get_all_fans, params=query, headers=config.headers).json()
    for user_info in response['data']:
        writer.writerow([user_info["user_id"], user_info["username"], user_info['full_name'], user_info['total_follow']])
