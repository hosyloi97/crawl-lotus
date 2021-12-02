import config_token as ct
import requests
import url_constant

# authorization
authorization = ct.token
session_id = '342c2bfa78b881415c7ee22fad344d3b0000017d0a824fe5'
cookie = '__uif=__uid%3A8965020032883629812; __RC=4; _kh_d_guid=74be05edbc125634d51434ce7b9e4410; __admUTMtime=1636558674; lotus=CfDJ8BfWuB4aSwJFvEVXTykf1UN0gBXLX31yh7xrWF3Oop3AxnZ1c6l_T_yw2Re0Wpri32yHTPVvHXoEcql5Er91MmuTCXKZPQ7UrUcTRZML89_CaCIvjq4nITNccNsY7bXs5h6WB19bcfvObfN4iZ2y4ST62FcN7_JHZvWnXTlo5GzQK1wJbjUlpIF2zSGEpsPTzldEfAspZgO-XgUMkvi7FBdm1tnINIfZqtaIIPX91PZbIa-bL3YdU_i6q6UKUZmFDtITKvPCmqv2Fk72LkVW11SWRA9kUrt48_g69x_1MlJ29PCshTRVO_LDSXws-hjtvVP-qqmtiamLOGMzPXRH4ihkvPRpd4wyjBTVlWBSeBa6okS3gGg9ccsO1wl_k0gSyHUn4KRc_3U9gdoe0_hTiBja5e0pSzuayYHxU3FNkmkdAfTbEWs5SH8dL2P7e2fZJ5cnOO_MNtpS590OGhHHclaaShZnwmBH-yRII2_OXdwfR3mnzqGHLcZfmHJUQdyv_JCsoZZp7lfHZrWVraAHzg57LN4fULu0F6WRSdOV_MMe7LSY9am_rU4s2Fb4UjpiOn9e7pW_4VtJMInpuOled7rEVSmYL4KNgH4YBtr0Ccf0nuIODrf8-T3O6TuoEaGP1wg4ToE90xcpCbmHoW9mqMfC1GxOxEbWGciM3O5kKDyWP-Q6gnHAr-3SXSqvArzL-xQB_H9vN7locUkJ-uI6c5lXcxItTCuwMicerUnAIbSqkMLdgeFhoJAvosIjq8U1AWllOItGSXljgxezEXvg_HZVVkIGY_Sh2OozHkKjzJodb0l8qNXjM8FA1XXrfCqhyqt0aIgsN81A57TBkUSrYgJXMwipk0yDr8_AbL4dFgRJBLANijEy6YX4OiPf0ucYr_gwsztAHGIFG-4JEXUlJ1FSvlW6IxrasFjG5nTOqa2eSyBg6scXRkQRvAkm39mT44TVo9EZyprcPrZiZqKY3J2dmYHSvNsg9IujIyJ8iAi2kwEjnnuAv8tC05gObI7nQBxbSbej1zi8PDjYGPjNRYBkcaQWRTl-sKV8wXLMCKhWeLxrQlSzQk5g5aEwsSm7gGf15QbZs4PgOh7FItGhEU5Sid7fys54Nfurf1FHfzDRs6IeUJGa1hFtOVycXwoAAtLCeRy3NnLv6g1TCEoZrcElqipapkaMF0o3NZsAe17UgEekVCEpAulixUIxN8Pn2CS0vnaFqZ_CmqYR6_EFv-j6LYWkq7lQ6gdLM42wdDLeJe2PnkYjG0GRXFPMSko3fzL_G6NHUVH930U8MH1I-Brd7TmKfXwMijkBvPqxRmw35w4hqpdM5Xh88eTg6oZQj2ng57GtjSWL12UzfhRadRWDMXPsNNui3cLjr8BLtuwSzSfaQDPH2l9GMvYjyCe0LVjTVZ6Ae_QOQoKuc9d-CpesrZ8ggOFDkEel_kApu6E7_WhLW1pjbtn_F-QvS3IyuAI6AYUYvXZQZLCySdLKv-EmiQYjnEYZQJgKLu8lvFhpoQvGKZr0g3ZdmyAttSlzxTHG8Mnt6kQHGXirKV4PtKQyM9ysmz51T2JDPU3oYGWzlrjUsnmYjobqNEKbytd9asdR6Oc0qkAtScCHo_RPMvu00e0vFceo3oPXvXD7UBfj3vNC0HwqLDdmgLTeZftWCC4-qyMr3cM3nun6ZugDb6_cJ6brFgqnS-Odb92e3h-Q; _lt_sd=PwdfIiFSBSsbFh4VKQk8UDlRRGtFK0RwdT8CWQ0/cB12VRAwEwdEcgNSAw0xJiELexsLOAkBXzQXHQ4dLDcxVToaED9IDV8+Xl8CFCQxNx4hRwMjSRZYNxtcSQw2MyBuPVBEa0VeDmcNR1JKcG9gBGYDXmRTVBR8GwMOCjY/PV89UERrRVUCYlpCCR8kYWpTbAxXZVZTVWdcFVlLIzc2AmAAAmIFVgZgCUBaTiFmMwlmAAA0UkRL; _ck_px_be=PwdfIiFSBWMNQghLJzAzBmxWXmlWUgdlWkcOHHdkNFAwB1JlA1VUYAlAW0l0YTYBNQxUZQEDAw=='

# my account
my_id = 88747935925278542

# init some variable
headers = {'authorization': authorization, 'session-id': session_id, 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
token_variable = '_kh_t_e_a_s'


def get_new_token():
    _headers_with_cookie = {'cookie': cookie}
    response = requests.get(url_constant.get_new_token, headers=_headers_with_cookie)
    cookie_str = str(response.headers.get('set-cookie'))
    return "Bearer " + str(cookie_str.split('=', 1)[1]).split(';', 1)[0]


def refresh_token():
    file_name = 'config_token.py'
    _token = get_new_token()
    with open(file_name, 'w') as f:
        f.write("token = '" + _token + "'")
        print('--------------Your token refreshed!----------------')
    return _token


def update_variable_value(self):
    self.authorization = refresh_token()
    self.headers = {'authorization': self.authorization, 'session-id': self.session_id}
