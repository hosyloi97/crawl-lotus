def convert_user_info(_user_info, _source_user_id=-1):
    if _source_user_id == -1:
        return userInfo(_user_info["user_id"], _user_info["username"], _user_info['fullName'],
                        _user_info['total_follow'], _source_user_id)
    else:
        return userInfo(_user_info["user_id"], _user_info["username"], _user_info['full_name'],
                        _user_info['total_follow'], _source_user_id)


class userInfo:
    def __init__(self, user_id, username, full_name, total_follow, source_user_id=-1):
        self.user_id = user_id
        self.username = username
        self.full_name = full_name
        self.total_follow = total_follow
        self.source_user_id = source_user_id
