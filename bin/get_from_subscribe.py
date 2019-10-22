import base64
from urllib import request

from bin import get_ssr_properties
from bin.ParseSsr import cleanupBase64


def get_from_subscribe():
    properties = get_ssr_properties.get_properties()
    to_test_url = []
    for serverSubscribe in properties['serverSubscribes']:
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        f = request.Request(serverSubscribe['URL'], headers=headers)
        ssr_subscribe = request.urlopen(f).read().decode('utf-8')  # 获取ssr订阅链接中数据
        ssr_subscribe_decode = base64.urlsafe_b64decode(cleanupBase64(ssr_subscribe)).decode('utf-8')
        to_test_url.extend(ssr_subscribe_decode.split('\n'))


if __name__ == '__main__':
    get_from_subscribe()
