import requests
import csv
import config as config
import url_constant
import user_info

# init value of params

no_page = 1
dev = 0

follower_file_name = 'follow_relationship.csv'
follow_relationship_column = ['user_id', 'follower_id']

user_info_file_name = 'user_info.csv'
user_info_column = ['user_id', 'username', 'full_name', 'total_follow', 'total_follower']


# # config for write to file csv
def get_my_followers(_writer_follow_f, _writer_user_f, _user_ids_scanned):
    # firstly, get all my followers info
    query = {'user_id': config.my_id, 'partner_id': config.my_id, 'no_page': no_page, 'dev': dev}
    my_followers = []
    response = call_api_and_auto_update_token(url_constant.get_all_followers, query, config.headers, config)
    for follower_info in response.json()['data']:
        my_followers.append(follower_info["user_id"])
        write_user_info(_writer_user_f, follower_info, False)
        _writer_follow_f.writerow([config.my_id, follower_info["user_id"]])
    _user_ids_scanned.append(config.my_id)
    return my_followers


def call_and_write_user_info(_user_id, _partner_id, _writer_user_f):
    query = {'user_id': _user_id, 'partner_id': _partner_id, 'no_page': no_page, 'dev': dev}
    response = call_api_and_auto_update_token(url_constant.get_detail_user_info, query, config.headers, config)
    _user_info = dict(response.json()["data"])
    write_user_info(_writer_user_f, _user_info, True)


# def call api and update authorization if 401:
def call_api_and_auto_update_token(_url, _params, _headers, _config):
    _response = requests.get(url=_url, params=_params, headers=_headers)
    if _response.__getattribute__('status_code') != 200:
        _config.update_variable_value(self=_config)
        _response = requests.get(url=_url, params=_params, headers=_headers)
    return _response


def write_user_info(_writer_user_f, _user_info, _is_self):
    if _is_self:
        _writer_user_f.writerow([_user_info["user_id"], _user_info["username"], _user_info['fullName'],
                                 _user_info['total_follow'], _user_info['total_follower']])
    else:
        _writer_user_f.writerow([_user_info["user_id"], _user_info["username"], _user_info['full_name'],
                                 _user_info['total_follow']])


def add_info_to_list(_list, _user_info, _is_myself=False):
    if _is_myself:
        _list.append(user_info.userInfo(_user_info["user_id"], _user_info["username"], _user_info['fullName'], _user_info['total_follow']))
    else:
        _list.append({"user_id": _user_info["user_id"], "username": _user_info["username"],
                     "full_name": _user_info['full_name'], "total_follow": _user_info['total_follow']})


user_ids_scanned = []
result = []
need_scan_ids = []
depth = 2


def scan_my_account(_user_ids_scanned, _need_scan_ids, _depth_index, _result):
    _params = {'user_id': config.my_id, 'partner_id': config.my_id, 'no_page': no_page, 'dev': dev}
    _response = call_api_and_auto_update_token(url_constant.get_detail_user_info, _params, config.headers, config)
    _user_info = dict(_response.json()["data"])
    add_info_to_list(_result, _user_info, True)
    _my_followers = _user_info['list_user_follow']
    if len(_my_followers) > 0:
        for _my_follower_info in _my_followers:
            _need_scan_ids.append(_my_follower_info['user_id'])
    _user_ids_scanned.append(config.my_id)
    _depth_index += 1


def main():
    depth_index = 1
    scan_my_account(user_ids_scanned, need_scan_ids, depth_index, result)
    while depth_index <= depth or len(need_scan_ids) > 0:

    print('depth index: ', depth_index)


main()
print(user_ids_scanned)
print(need_scan_ids)

# def write_data():
#     follow_f = open(follower_file_name, 'w')
#     writer_follow_f = csv.writer(follow_f)
#     writer_follow_f.writerow(follow_relationship_column)
#
#     user_f = open(user_info_file_name, 'w')
#     writer_user_f = csv.writer(user_f)
#     writer_user_f.writerow(user_info_column)
#     call_and_write_user_info(config.my_id, config.my_id, writer_user_f)
#
#     my_followers_ids = get_my_followers(writer_follow_f, writer_user_f, user_ids_scanned)
#     print(my_followers_ids)
#
#     follow_f.close()
#     user_f.close()
#
#
# write_data()
