import requests

import config as config
import url_constant
import user_info
import util


# get followers by paging
def get_followers(_target_user_id, _no_page, _dev, _stop_loop_index=0):
    if 0 < _stop_loop_index <= _no_page:
        return []
    query = {'user_id': config.my_id, 'partner_id': _target_user_id, 'no_page': _no_page, 'dev': _dev}
    list_followers = []
    response = util.call_api_and_auto_update_token(url_constant.get_all_fans, query)
    _followers = []
    try:
        _followers.extend(response.json()['data'])
    except:
        util.log_method("get_followers", "ERROR at id: {}".format(_target_user_id))
        return []
    for _follower_info in _followers:
        list_followers.append(user_info.convert_user_info(_follower_info, _target_user_id))
    return list_followers


def get_all_followers(_target_user_id):
    _loop_index = 1
    _still_loop = True
    _list_followers = []
    _no_page = 1
    _dev = 0
    util.log_method("get_all_followers", "scanning fans for {}".format(_target_user_id))
    while _still_loop:
        _followers = get_followers(_target_user_id, _no_page, _dev, 2)
        if len(_followers) > 0:
            _list_followers.extend(_followers)
            _no_page += 1
            _loop_index += 1
        else:
            _still_loop = False
    util.log_method_complete("get_all_followers",
                             "Scanning followers for {} successfully with {} fans".format(_target_user_id,
                                                                                          len(_list_followers)))
    return _list_followers
