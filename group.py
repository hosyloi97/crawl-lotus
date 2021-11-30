import url_constant
import util


def get_members_of_group_by_paging(_group_id, _type=1):
    _params = {'group_id': _group_id, 'type': _type}
    _response = util.call_api_and_auto_update_token(url_constant.get_members_of_group, _params)
    return _response.json()['data']['members']


def get_all_members_of_group(_group_id):
    _members = get_members_of_group_by_paging(_group_id)
    _list_members = []
    if len(_members) > 0:
        for _member in _members:
            _list_members.append(_member['member_id'])
    return _list_members
