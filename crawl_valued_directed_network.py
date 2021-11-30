import datetime as dt

import csv
import get_all_fans_of_user_id
import group
import user_info
import util
import post

# init value of params
no_page = 1
dev = 0
user_ids_scanned = []
result = []
need_scan_ids = []
depth = 1

follower_file_name = 'csv/follow_relationship.csv'
follow_relationship_column = ['index', 'user_id', 'follower_id', 'weight']
user_info_file_name = 'csv/user_info.csv'
user_info_column = ['index', 'user_id', 'username', 'full_name', 'total_follower']


def write_user_info(_index, _writer_user_f, _user_info):
    _writer_user_f.writerow([_index, _user_info.user_id, _user_info.username, _user_info.full_name,
                             _user_info.total_follow])


def write_follow_relationship_info(_index, _writer_follow_f, _user_info, _source_user_id):
    if _source_user_id != -1:
        _writer_follow_f.writerow([_index, _user_info.source_user_id, _user_info.user_id, _user_info.weight])


def scan_followers_by_user_id(_user_ids_scanned, _need_scan_ids, _depth_index, _result):
    _need_scan_ids_new = _need_scan_ids.copy()
    _need_scan_ids.clear()
    for _user_id_scanning in _need_scan_ids_new:
        if _user_id_scanning not in _user_ids_scanned:
            _list_fans = get_all_fans_of_user_id.get_all_followers(_user_id_scanning)
            # _map_user_id_with_reactions = post.get_all_posts_from_user_id(_user_id_scanning)
            _user_ids_scanned.append(_user_id_scanning)
            for _fan in _list_fans:
                _fan.__class__ = user_info.userInfo
                if _fan.user_id not in _user_ids_scanned:
                    _result.append(_fan)
                    _need_scan_ids.append(_fan.user_id)


def crawl_data():
    util.log_method("crawl_data", "depth : {}".format(depth), 1)
    depth_index = 1
    _group_id = 867635381098110976

    need_scan_ids = group.get_all_members_of_group(_group_id=_group_id)

    while depth_index <= depth and len(need_scan_ids) > 0:
        scan_followers_by_user_id(user_ids_scanned, need_scan_ids, depth_index, result)
        print()
        print()
        print("<<<===================== Scanned with depth = {} success ==========================>>>".format(
            depth_index))
        print()
        print()
        depth_index += 1
    print("===================== scanned {} actors ==========================".format(len(user_ids_scanned)))
    util.log_method_complete("crawl_data", "", 1)


def write_data():
    util.log_method("write_data", "", 1)
    _follow_f = open(follower_file_name, 'w')
    _writer_follow_f = csv.writer(_follow_f)
    _writer_follow_f.writerow(follow_relationship_column)

    _user_f = open(user_info_file_name, 'w')
    _writer_user_f = csv.writer(_user_f)
    _writer_user_f.writerow(user_info_column)

    _index = 1
    _index_user_info = 1
    _user_info_detail_wrote = []
    for _user_info in result:
        _user_info.__class__ = user_info.userInfo
        write_follow_relationship_info(_index, _writer_follow_f, _user_info, _user_info.source_user_id)
        if _user_info.user_id not in _user_info_detail_wrote:
            write_user_info(_index_user_info, _writer_user_f, _user_info)
            _user_info_detail_wrote.append(_user_info.user_id)
            _index_user_info += 1
        _index += 1
    _follow_f.close()
    _user_f.close()
    util.log_method_complete("write_data", "", 1)


start_time = dt.datetime.now()
crawl_data()
write_data()
end_time = dt.datetime.now()
print("Running start from {} to {}".format(start_time, end_time))
