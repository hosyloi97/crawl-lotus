import requests
# import csv
import config as config
import url_constant

# init value of params

# follower_file_name = 'follow_relationship.csv'
# follow_relationship_column = ['user_id', 'follower_id']
#
# user_info_file_name = 'user_info.csv'
# user_info_column = ['user_id', 'username', 'full_name', 'total_follow', 'total_follower']


# # config for write to file csv
# def get_followers(_writer_follow_f, _writer_user_f, _user_ids_scanned, _target_user_id):
#     query = {'user_id': config.my_id, 'partner_id': _target_user_id, 'no_page': no_page, 'dev': dev}
#     my_followers = []
#     response = call_api_and_auto_update_token(url_constant.get_all_followers, query, config.headers, config)
#     for follower_info in response.json()['data']:
#         my_followers.append(follower_info["user_id"])
#         write_user_info(_writer_user_f, follower_info, False)
#         _writer_follow_f.writerow([config.my_id, follower_info["user_id"]])
#     _user_ids_scanned.append(config.my_id)
#     return my_followers

# get followers by paging
import user_info


def get_followers(_target_user_id, _no_page, _dev, _stop_loop_index=0):
    if 0 < _stop_loop_index <= _no_page:
        return []
    print('---------- Loop index : ', _no_page)
    query = {'user_id': config.my_id, 'partner_id': _target_user_id, 'no_page': _no_page, 'dev': _dev}
    list_followers = []
    response = call_api_and_auto_update_token(url_constant.get_all_fans, query, config.headers, config)
    _followers = response.json()['data']
    if len(_followers) == 0:
        print(str(target_user_id) + ' has no public fans')
    for _follower_info in _followers:
        list_followers.append({"user_id": _follower_info["user_id"], "username": _follower_info["username"],
                               "full_name": _follower_info['full_name'],
                               "total_follow": _follower_info['total_follow']})
    print('---------- Loop index : ', _no_page, ' end. Found ', len(list_followers), ' fans -------------')
    return list_followers


def get_all_followers(_target_user_id):
    _loop_index = 1
    _still_loop = True
    _list_followers = []
    _no_page = 1
    _dev = 0
    while _still_loop:
        _followers = get_followers(_target_user_id, _no_page, _dev)
        if len(_followers) > 0:
            _list_followers.extend(_followers)
            _no_page += 1
            _loop_index += 1
        else:
            _still_loop = False
    return _list_followers


# def call api and update authorization if 401:
def call_api_and_auto_update_token(_url, _params, _headers, _config):
    _response = requests.get(url=_url, params=_params, headers=_headers)
    if _response.__getattribute__('status_code') != 200:
        _config.update_variable_value(self=_config)
        _response = requests.get(url=_url, params=_params, headers=_headers)
    return _response


target_user_id = 17245262652958830
total_fans = get_all_followers(target_user_id)
print(str(target_user_id), ' has ', len(total_fans), ' fans')
print(total_fans)

# def write_user_info(_writer_user_f, _user_info, _is_self):
#     if _is_self:
#         _writer_user_f.writerow([_user_info["user_id"], _user_info["username"], _user_info['fullName'],
#                                  _user_info['total_follow'], _user_info['total_follower']])
#     else:
#         _writer_user_f.writerow([_user_info["user_id"], _user_info["username"], _user_info['full_name'],
#                                  _user_info['total_follow']])
#

# def write_data(_user_ids_scanned):
#     follow_f = open(follower_file_name, 'w')
#     writer_follow_f = csv.writer(follow_f)
#     writer_follow_f.writerow(follow_relationship_column)
#
#     user_f = open(user_info_file_name, 'w')
#     writer_user_f = csv.writer(user_f)
#     writer_user_f.writerow(user_info_column)
#
#     get_followers(writer_follow_f, writer_user_f, _user_ids_scanned)
#
#     follow_f.close()
#     user_f.close()


# user_ids_scanned = []
# write_data(user_ids_scanned)
# print(user_ids_scanned)
