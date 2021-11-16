import requests
import config as config
import datetime


def call_api_and_auto_update_token(_url, _params, _headers=config.headers):
    _response = requests.get(url=_url, params=_params, headers=_headers)
    if _response.__getattribute__('status_code') != 200:
        config.update_variable_value(self=config)
        _response = requests.get(url=_url, params=_params, headers=config.headers)
    return _response


def log_method(_method_name, params="",_number_enter=0):
    print("=========== START {} ================".format(get_log_message(_method_name, params)))
    if _number_enter != 0:
        print()


def log_method_complete(_method_name, _params="", _number_enter=0):
    if _number_enter != 0:
        print()
    print("=========== [{}] END {} ================".format(datetime.datetime.now(),
                                                            get_log_message(_method_name, _params)))


def get_log_message(_method_name, _params=""):
    if _params != "":
        return " {} with {} ".format(_method_name, _params)
    else:
        return _method_name
