import util
import url_constant
import emotion
import datetime as dt

# init quantity loop
max_loop = 8


def get_posts_by_paging(_target_user_id, _page, _max_loop=0, _numnews=50, _reload=1, _post_id=0, _type=0):
    if 0 < _max_loop < _page:
        return []
    params = {'numnews': _numnews, 'reload': _reload, 'page': _page, 'guid': _target_user_id, 'postid': _post_id,
              'type': _type}
    response = util.call_api_and_auto_update_token(url_constant.get_all_posts, params)
    return response.json()['result']['data']


def get_all_posts_from_user_id(_target_user_id):
    _loop_index = 1
    _still_loop = True
    _list_posts = []
    _list_original_posts = []
    _page = 1
    util.log_method("get_all_posts_from_user_id", "scanning posts for {}".format(_target_user_id))
    while _still_loop:
        _posts = get_posts_by_paging(_target_user_id, _page, max_loop)
        if len(_posts) > 0:
            _list_original_posts.extend(_posts)
            _page += 1
            _loop_index += 1
        else:
            _still_loop = False
    if len(_list_original_posts) > 0:
        for _post in _list_original_posts:
            _list_posts.append(Post(_post['id'], _post['media_id'], _post['publish_date']))
    util.log_method_complete("get_all_posts_from_user_id",
                             "Scanning posts for {} successfully with {} posts".format(_target_user_id,
                                                                                       len(_list_posts)))
    return _list_posts


def get_quantity_react_of_fans_to_user(_target_user_id):
    _list_posts = get_all_posts_from_user_id(_target_user_id)
    _result = {}
    _users = []
    if len(_list_posts) > 0:
        for _post in _list_posts:
            _post_id = _post.id
            _users.extend(emotion.get_all_users_react(_post_id))
        if len(_users) > 0:
            for _user in _users:
                _result[_user] = _result.get(_user, 0) + 1
    return _result


class Post:
    def __init__(self, _id, _media_id, _publish_date):
        self.id = _id
        self.media_id = _media_id
        self.publish_date = _publish_date


start_time = dt.datetime.now()
res = get_quantity_react_of_fans_to_user(18241256567433054)
end_time = dt.datetime.now()
print("Running start from {} to {}".format(start_time, end_time))
