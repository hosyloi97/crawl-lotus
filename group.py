import url_constant
import util

# default get 20 lements
def get_members_of_group_by_paging(_group_id, _type=1):
    _params = {'group_id': _group_id, 'type': _type}
    _response = util.call_api_and_auto_update_token(url_constant.get_members_of_group, _params)
    return _response.json()['data']['members']


def get_all_members_of_group(_group_id, _list=None):
    if _list is None:
        _list = []
    _members = get_members_of_group_by_paging(_group_id)
    if len(_members) > 0:
        for _member in _members:
            _list.append(_member['member_id'])
    return _list
