import base64
from urllib import request

from foo import ssr_properties
from foo.parse_url import cleanupBase64


def get_from_subscribe():
    properties = ssr_properties.get_properties()
    to_test_url = []
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    for serverSubscribe in properties['serverSubscribes']:
        try:
            f = request.Request(serverSubscribe['URL'], headers=headers)
            ssr_subscribe = request.urlopen(f).read().decode('utf-8')  # 获取ssr订阅链接中数据
            ssr_subscribe_decode = base64.urlsafe_b64decode(cleanupBase64(ssr_subscribe)).decode('utf-8')
            to_test_url.extend(ssr_subscribe_decode.split('\n'))
        except Exception:
            continue
    return to_test_url


if __name__ == '__main__':
    get_from_subscribe()
