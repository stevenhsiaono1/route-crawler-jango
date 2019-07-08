import requests
import json
import time
from fake_useragent import UserAgent


def get_data(url, i):
    ua = UserAgent()
    # HEADERS = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
    #                       'AppleWebKit/537.36 (KHTML, like Gecko)'
    #                       'Chrome/45.0.2454.101 Safari/537.36'),
    #                       'referer': 'http://marrydorry.pixnet.net/blog'}
    HEADERS = {'user-agent':str(ua.random), 'referer': 'http://marrydorry.pixnet.net/blog'}
    response = requests.get(url, HEADERS)
    if response.status_code == 200:
        return True
    else:
        print(response.text)
        print(response.status_code)

for i in range(100): # 30 NBA Teams
    base_url = "https://marrydorry.pixnet.net/blog/post/278676524"
    data = get_data(base_url, i)
    print(i)
    time.sleep(10)

