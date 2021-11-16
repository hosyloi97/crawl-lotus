import csv
from datetime import date

import util
import config as config
import get_all_fans_of_user_id
import url_constant
import user_info

# init value of params
no_page = 1
dev = 0
user_ids_scanned = []
result = []
need_scan_ids = []
depth = 3

follower_file_name = 'follow_relationship.csv'
follow_relationship_column = ['index', 'user_id', 'follower_id']
user_info_file_name = 'user_info.csv'
user_info_column = ['index', 'user_id', 'username', 'full_name', 'total_follower']


def write_user_info(_index, _writer_user_f, _user_info):
    _writer_user_f.writerow([_index, _user_info.user_id, _user_info.username, _user_info.full_name,
                             _user_info.total_follow])


def write_follow_relationship_info(_index, _writer_follow_f, _user_info, _source_user_id):
    if _source_user_id != -1:
        _writer_follow_f.writerow([_index, _user_info.source_user_id, _user_info.user_id])


def scan_my_account(_user_ids_scanned, _need_scan_ids, _depth_index, _result):
    _params = {'user_id': config.my_id, 'partner_id': config.my_id, 'no_page': no_page, 'dev': dev}
    _response = util.call_api_and_auto_update_token(url_constant.get_detail_user_info, _params)
    _user_info = dict(_response.json()["data"])
    _result.append(user_info.convert_user_info(_user_info))
    _my_followers = _user_info['list_user_follow']
    if len(_my_followers) > 0:
        for _my_follower_info in _my_followers:
            _need_scan_ids.append(_my_follower_info['user_id'])
    _user_ids_scanned.append(config.my_id)
    _depth_index += 1
    util.log_method_complete("scan_my_account")


def scan_followers_by_user_id(_user_ids_scanned, _need_scan_ids, _depth_index, _result):
    _need_scan_ids_new = _need_scan_ids.copy()
    _need_scan_ids.clear()
    for _user_id_scanning in _need_scan_ids_new:
        if _user_id_scanning not in _user_ids_scanned:
            _list_fans = get_all_fans_of_user_id.get_all_followers(_user_id_scanning)
            _user_ids_scanned.append(_user_id_scanning)
            for _fan in _list_fans:
                _fan.__class__ = user_info.userInfo
                if _fan.user_id not in _user_ids_scanned:
                    _result.append(_fan)
                    _need_scan_ids.append(_fan.user_id)


def crawl_data():
    util.log_method("crawl_data", "depth : {}".format(depth), 1)
    depth_index = 1

    scan_my_account(user_ids_scanned, need_scan_ids, depth_index, result)
    while depth_index <= depth and len(need_scan_ids) > 0:
        scan_followers_by_user_id(user_ids_scanned, need_scan_ids, depth_index, result)
        depth_index += 1
    util.log_method_complete("crawl_data", "", 1)


def write_data():
    util.log_method("write_data", "", 1)
    follow_f = open(follower_file_name, 'w')
    writer_follow_f = csv.writer(follow_f)
    writer_follow_f.writerow(follow_relationship_column)

    user_f = open(user_info_file_name, 'w')
    writer_user_f = csv.writer(user_f)
    writer_user_f.writerow(user_info_column)

    index = 1
    for _user_info in result:
        _user_info.__class__ = user_info.userInfo
        write_user_info(index, writer_user_f, _user_info)
        write_follow_relationship_info(index, writer_follow_f, _user_info, _user_info.source_user_id)
        index += 1
    follow_f.close()
    user_f.close()
    util.log_method_complete("write_data", "", 1)


crawl_data()
write_data()
