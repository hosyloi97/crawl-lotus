import config
import url_constant
import util
import json


def get_list_user_react_post_with_paging(_post_id, _offset, _max_loop, _length=200, _type_react=0):
    _header = {'session-id': config.session_id, 'cookie': config.cookie, 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
    _params = {'postId': _post_id, 'type_react': _type_react, 'length': _length, 'offset': _offset}
    if 0 < _max_loop < _offset:
        return []
    try:
        _response = util.call_api_and_auto_update_token(url_constant.get_reactions_of_post, _params, _header)
        return json.loads(_response.json())['data']['lst_user']
    except:
        return []


def get_all_users_react(_post_id, _max_loop=1):
    _loop_index = 1
    _still_loop = True
    _list_user_reactions = []
    _response = []
    _page = 1
    util.log_method("get_all_users_react", "scanning list users reacted with post id: {}".format(_post_id))
    while _still_loop:
        _users = get_list_user_react_post_with_paging(_post_id, _page, _max_loop)
        if len(_users) > 0:
            _response.extend(_users)
            _page += 1
            _loop_index += 1
        else:
            _still_loop = False
    if len(_response) > 0:
        for _user in _response:
            _list_user_reactions.append(_user['user_id'])
    util.log_method_complete("get_all_users_react",
                             "Scanning list reacted user with post id: {} successfully with {} users".format(
                                 _post_id, len(_list_user_reactions)))
    return _list_user_reactions
