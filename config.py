import config_token as ct
import refresh_token

# authorization
authorization = ct.token
session_id = '342c2bfa78b881415c7ee22fad344d3b0000017d0a824fe5'

# my account
my_id = 88747935925278542

# init some variable
headers = {'authorization': authorization, 'session-id': session_id}
token_variable = '_kh_t_e_a_s'


def update_variable_value(self):
    new_authorization = refresh_token.refresh_token()
    self.authorization = new_authorization
    self.headers = {'authorization': new_authorization, 'session-id': session_id}

