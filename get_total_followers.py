import util

import config as config
import url_constant

# init value of params

no_page = 1
dev = 0


def get_total_followers_quantity(_target_user_id):
    params = {'user_id': config.my_id, 'partner_id': _target_user_id, 'no_page': no_page, 'dev': dev}
    response = util.call_api_and_auto_update_token(url_constant.get_detail_user_info, params)
    return response.json()['data']['total_follower']
