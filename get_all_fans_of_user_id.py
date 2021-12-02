import post
import config as config
import url_constant
import user_info
import util


# get followers by paging
def get_followers(_target_user_id, _no_page, _dev, _stop_loop_index=0):
    if 0 < _stop_loop_index < _no_page:
        return []
    query = {'user_id': config.my_id, 'partner_id': _target_user_id, 'no_page': _no_page, 'dev': _dev}
    list_followers = []
    response = util.call_api_and_auto_update_token(url_constant.get_all_fans, query)
    try:
        list_followers.extend(response.json()['data'])
    except:
        util.log_method("get_followers", "ERROR at id: {}".format(_target_user_id))
    return list_followers


def get_reactions_from_map(_map, _follower_id):
    _reactions = 0
    if len(_map) > 0:
        _reactions = _map.get(_follower_id)
    return _reactions if _reactions is not None else 0


def get_all_followers(_target_user_id, _depth=1):
    _loop_index = 1
    _still_loop = True
    _list_followers = []
    _no_page = 1
    _dev = 0
    util.log_method("get_all_followers", "scanning fans for {}".format(_target_user_id))
    _list_term = []
    _map = {}
    while _still_loop:
        _followers = get_followers(_target_user_id, _no_page, _dev, _depth)
        if len(_followers) > 0:
            _list_term.extend(_followers)
            _no_page += 1
            _loop_index += 1
        else:
            _still_loop = False
    if len(_list_term) > 0:
        _map = post.get_quantity_react_of_fans_to_user(_target_user_id, 2)
        for _follower in _list_term:
            _follower_id = _follower['user_id']
            _list_followers.append(
                user_info.convert_user_info(_follower, get_reactions_from_map(_map, _follower_id), _target_user_id))
    util.log_method_complete("get_all_followers",
                             "Scanning followers for {} successfully with {} fans".format(_target_user_id,
                                                                                          len(_list_followers)))
    return _list_followers
