import requests
import config as config
import url_constant

# init value of params

no_page = 1
dev = 0


# def call api and update authorization if 401:
def call_api_and_auto_update_token(_url, _params, _headers, _config):
    _response = requests.get(url=_url, params=_params, headers=_headers)
    if _response.__getattribute__('status_code') != 200:
        _config.update_variable_value(self=_config)
        _response = requests.get(url=_url, params=_params, headers=_headers)
    return _response


def get_total_followers_quantity(_target_user_id):
    params = {'user_id': config.my_id, 'partner_id': _target_user_id, 'no_page': no_page, 'dev': dev}
    response = call_api_and_auto_update_token(url_constant.get_detail_user_info, params, config.headers, config)
    return response.json()['data']['total_follower']
